from django.dispatch import receiver
from django.db.models.signals import post_save
from services.tasks import send_payment_notification
from django.core.cache import cache
from django.conf import settings

from payment.models import Collect


@receiver(post_save, sender=Collect)
def post_save_send_notification(**kwargs):
    '''Отправляем уведомление по почте адресатуб,
    а выполняем инвалидацию кеширования'''

    instance = kwargs['instance']
    send_payment_notification(instance)
    cache.delete(settings.GET_CACHE_COLLECT)

