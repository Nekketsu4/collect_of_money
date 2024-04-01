from celery import shared_task

from payment.models import Payment
from collect.models import Collect


@shared_task()
def get_sum_count(collect_id):
    get_collect = Collect.objects.get(pk=collect_id)
    for payment in get_collect.payments.all():
        summ = sum(payment.pay_amount)