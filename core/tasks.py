from celery import shared_task
from django.core.mail import send_mail

from celery_send_email.settings import EMAIL_HOST_USER

@shared_task
def send_email_task():
    from_email = EMAIL_HOST_USER
    send_mail('test subject', 'test message', from_email, ['cidebeb172@goqoez.com'])
    return None
