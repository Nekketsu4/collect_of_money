from django.contrib.auth.models import User
from collect.models import Collect
from django.db import models
from payment.tasks import send_payment_notification


class Payment(models.Model):

    CARDS = (
        (None, 'Выберите карту'),
        ('sber', 'Сбербанк'),
        ('alpha', 'Альфа-банк'),
        ('tinkoff', 'Тинькофф')
    )

    card = models.CharField('Способ оплаты', max_length=32, choices=CARDS, default=None)
    pay_amount = models.IntegerField('Сумма оплаты', default=0, blank=False)
    owner = models.ForeignKey(User, related_name='another', on_delete=models.CASCADE)
    date_pay = models.DateTimeField('Время и дата оплаты', auto_now_add=True)
    collect = models.ForeignKey(Collect, related_name='payments', on_delete=models.CASCADE)

    def save(self, *args, save_model=True, **kwargs):
        if save_model:
            send_payment_notification.delay(
                self.owner.first_name,
                self.collect.title,
                self.owner.email
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'Оплата на сумму {self.pay_amount} руб. Оплатил {self.owner.username} - {self.date_pay}'


