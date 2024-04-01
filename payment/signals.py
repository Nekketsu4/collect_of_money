from django.dispatch import receiver
from django.db.models.signals import post_save
from services.tasks import send_payment_notification

from payment.models import Payment


@receiver(post_save, sender=Payment)
def post_save_send_notification(**kwargs):

    """Отправляем уведомление адресату по почте
     о выполнении платежа"""

    instance = kwargs['instance']
    send_payment_notification(instance)
