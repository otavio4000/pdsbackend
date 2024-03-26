from django.db.models.signals import post_save, pre_delete, m2m_changed
from django.contrib.auth.models import User
from django.dispatch import receiver
from medida_tomada.models import MedidaTomada
from alunos.models import Aluno
from denuncia.models import Denuncia
from .models import Notification
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail

@receiver(post_save, sender=MedidaTomada)
def create_notification_on_medidatomada_creation(sender, instance, created, **kwargs):
    if created:
        denuncia = instance.denuncia_id
        responsaveis_email = set()

        # Adicione os responsáveis dos alunos envolvidos na denúncia aos responsáveis
        responsaveis_email.update(denuncia.vitimas.all().values_list('responsaveis__user__email', flat=True))
        responsaveis_email.update(denuncia.praticantes.all().values_list('responsaveis__user__email', flat=True))
        
        subject = "Atualização de denúncia de dependente"
        txt = f"""<html>
    <body>
        <p>Uma denúncia na qual seu depente está envolvido sofreu uma alteração</p>
        <p> <b>Título da denúncia </b>: {denuncia.titulo}</p>
        <p><a href="https://pds-2023-2-two.vercel.app/login">Clique aqui para ver mais detalhes</a></p>
    </body>
    </html>
        """

# Crie uma notificação para cada responsável

    for email in responsaveis_email:
    
        recipient_list = email
    
        try:
        
            sent_mail = send_mail(
            subject,
            '',
            "vigialuno@gmail.com",
            [recipient_list],  
            html_message=txt,  
            fail_silently=False,
        )
        
        except Exception as e:
            print(e)
            # message = f'Nova medida tomada para a denúncia "{denuncia.titulo}": {instance.acao}'
            # Notification.objects.create(user=user, medida_tomada=instance, message=message)


@receiver(m2m_changed, sender=Denuncia.vitimas.through)
@receiver(m2m_changed, sender=Denuncia.praticantes.through)
def create_notification_on_denuncia_association_change(sender, instance, action, model, pk_set, **kwargs):
    if action == 'post_add':
        
        responsaveis_email = set()
        
        # Obter os responsáveis dos alunos recém-adicionados
        for aluno_id in pk_set:
            aluno = model.objects.get(id=aluno_id)
            responsaveis_email.update(aluno.responsaveis.values_list('user__email', flat=True))

        # Criar uma notificação para cada responsável dos novos alunos adicionados
        txt = f"""<html>
    <body>
        <p>Um dependente seu está envolvido em uma nova denúncia.</p>
        <p> <b>Título da denúncia </b>: {instance.titulo}</p>
        <p><a href="https://pds-2023-2-two.vercel.app/login">Clique aqui para ver mais detalhes</a></p>
    </body>
    </html>
        """
        subject = "Atualização de envolvimento  de dependente"
        for email in responsaveis_email:
            print(email)

            recipient_list = email
            try:
        
                sent_mail = send_mail(
                subject,
                '',
                "vigialuno@gmail.com",
                [recipient_list],  
                html_message=txt,  
                fail_silently=False,
                )   
        
                
            
            except  Exception as e:
               print(e)
            # message = f'Um dependente seu está envolvido em uma nova denúncia: {instance.titulo}'
            # Notification.objects.create(user=responsavel.user, denuncia=instance, message=message)