from django.core.mail import send_mail
from server.settings import EMAIL_HOST

from celery import shared_task


@shared_task()
def send_collect_notification(first_name, title, mail):
    send_mail(
        subject='Операция успешно выполнена',
        message=f'Здравствуйте {first_name}! Сбор денежных средст на {title}, успешно создан!',
        from_email=EMAIL_HOST,
        recipient_list=[mail, ]
    )
