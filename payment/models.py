from django.contrib.auth.models import User
from collect.models import Collect
from django.db import models


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
    pay_for_collect = models.ForeignKey(Collect, related_name='payments', on_delete=models.CASCADE)

    def __str__(self):
        return f'Оплата на сумму {self.pay_amount} руб. Оплатил {self.owner.username} - {self.date_pay}'


