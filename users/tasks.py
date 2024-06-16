from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse

domain = settings.DOMAIN_NAME


@shared_task
def send_reset_email(email, token):
    email_plaintext_message = (
        "Для сброса пароля перейдите по ссылке: {}{}?token={}".format(
            domain, reverse("password_reset:reset-password-confirm"), token
        )
    )

    send_mail(
        # title:
        "Сброс пароля для: {title}".format(title="EDO website"),
        # message:
        email_plaintext_message,
        # from:
        settings.EMAIL_HOST_USER,
        # to:
        [email],
    )
