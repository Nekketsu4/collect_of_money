from django.contrib.auth.models import User
from collect.models import Collect
from django.db import models
# from payment.tasks import send_payment_notification


class Payment(models.Model):

    pay_amount = models.IntegerField(
        'Сумма оплаты',
        default=0,
        blank=False
    )

    owner = models.ForeignKey(
        User,
        related_name='user_payment',
        on_delete=models.CASCADE
    )

    date_pay = models.DateTimeField(
        'Время и дата оплаты',
        auto_now_add=True
    )

    collect = models.ForeignKey(
        Collect,
        related_name='collect_payment',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Оплата на сумму {self.pay_amount} руб. Оплатил {self.owner.username} - {self.date_pay}'
