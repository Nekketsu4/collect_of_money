from django.core.mail import send_mail
from server.settings import EMAIL_HOST

from celery import shared_task


@shared_task()
def send_payment_notification(first_name, title, mail):
    send_mail(
        subject='Операция успешно выполнена',
        message=f'Здравствуйте {first_name}! Платеж для сбора денег на {title}',
        from_email=EMAIL_HOST,
        recipient_list=[mail, ]
    )
