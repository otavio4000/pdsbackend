from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import send_mail

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    
    reset_password_url= "{}?token={}".format(
        instance.request.build_absolute_uri(reverse('password_reset:reset-password-confirm')),
        reset_password_token.key)


    subject = "Redefinição de Senha para sua conta na plataforma Vigialuno"
    message = (
        f"Olá {reset_password_token.user.first_name} {reset_password_token.user.last_name},\n\n"
        "Você está recebendo este e-mail porque foi solicitada uma redefinição de senha para sua conta "
        f"com o email {reset_password_token.user.email}.\n\n"
        "Por favor, clique no link abaixo para redefinir sua senha:\n"
        f"{reset_password_url}\n\n"
        f"Seu token é: {reset_password_token.key}.\n\n"
        "Se você não solicitou uma redefinição de senha, por favor, ignore este e-mail.\n\n"
        "Obrigado!"
    )

    # Send email
    from_email = 'vigialuno@gmail.com'
    to_email = [reset_password_token.user.email]
    send_mail(subject, message, from_email, to_email)
