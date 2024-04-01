from django.core.mail import send_mail
from server.settings import EMAIL_HOST

from celery import shared_task

from payment.models import Payment
from collect.models import Collect


@shared_task()
def send_payment_notification(instance):
    """ Отправляем письмо адресату по почте в зависимости от полученого сигнала """

    message = ""
    mail = ""

    if isinstance(instance, Collect):
        first_name = instance.author_collect.first_name
        title = instance.title
        mail = instance.author_collect.email
        message = f'Здравствуйте {first_name}! Сбор денежных средст на {title}, успешно создан!'

    if isinstance(instance, Payment):
        first_name = instance.owner.first_name
        title = instance.collect.title
        mail = instance.owner.email
        message = f'Здравствуйте {first_name}! Платеж для сбора денег на {title} выполнен'

    send_mail(
        subject='Операция успешно выполнена',
        message=message,
        from_email=EMAIL_HOST,
        recipient_list=[mail, ]
    )
