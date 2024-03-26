import uuid
from django.db import models
from alunos.models import Aluno
pontuacoes = {'v_fisica': 0.4, 'v_verbal': 0.1, 'bullying': 0.2, 'assedio': 0.6, 'v_domestica': 0.7}

CHOICES = (
        ('yes', 'Sim'),
        ('no', 'Não'),
    )


def upload_file_formater(instance, filename):
    return f"{str(uuid.uuid4())}--{filename}"
class Denuncia(models.Model):
    
    titulo = models.CharField(max_length = 100, blank=True)
    praticantes = models.ManyToManyField(Aluno, related_name='denuncia_praticante', blank=True)
    vitimas = models.ManyToManyField(Aluno, related_name='denuncia_vitima', blank=True)

    matricula = models.IntegerField()    
    relato = models.CharField(max_length = 500)
    lugar = models.CharField(max_length = 50)
    v_fisica = models.CharField(max_length = 10, choices=CHOICES)
    v_verbal = models.CharField(max_length = 10, choices=CHOICES)
    bullying = models.CharField(max_length = 10, choices=CHOICES)
    assedio =  models.CharField(max_length = 10, choices=CHOICES)
    recorrencia = models.CharField(max_length = 50)
    data_ocorrido = models.DateTimeField()
    
    v_domestica = models.CharField(max_length = 10, choices=CHOICES)
    telefone_1 = models.CharField(max_length = 15, blank=True, null=True)
    telefone_2 = models.CharField(max_length = 15, blank=True, null=True)

    arquivo_1 = models.FileField(upload_to=upload_file_formater, null=True, blank=True)
    arquivo_2 = models.FileField(upload_to=upload_file_formater, null=True, blank=True)
    arquivo_3 = models.FileField(upload_to=upload_file_formater, null=True, blank=True)

    data_denuncia = models.DateTimeField(auto_now_add=True)
    pontuacao = models.FloatField(default=0.0)
    status = models.CharField(max_length = 40, default='nao investigado')
    def save(self, *args, **kwargs):
            
            pontuacao = 0.0

            campos_para_pontuar = [
                self.v_fisica,
                self.v_verbal,
                self.bullying,
                self.assedio,
                self.v_domestica,
                
            ]

            if(self.v_fisica == 'yes'):
                pontuacao += pontuacoes['v_fisica']
            if(self.v_verbal == 'yes'):
                pontuacao += pontuacoes['v_verbal']
            if(self.bullying == 'yes'):
                pontuacao += pontuacoes['bullying']
            if(self.assedio == 'yes'):
                pontuacao += pontuacoes['assedio']   
            if(self.v_domestica == 'yes'):
                pontuacao += pontuacoes['v_domestica']         
            self.pontuacao = round(pontuacao,2)

            super(Denuncia, self).save(*args, **kwargs)