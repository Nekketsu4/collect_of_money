from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Collect(models.Model):

    REASONS = (
        (None, 'Выберите повод для сбора'),
        ('wedding', 'Свадьба'),
        ('birthday', 'День рождения'),
        ('funeral', 'Похороны')
    )

    author_collect = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Автор сбора')
    title = models.CharField('Название', max_length=200)
    reason = models.CharField('Повод для сбора', max_length=32, choices=REASONS)
    description = models.TextField('Опишите более подробно', blank=True)
    goal_collect = models.IntegerField('Сколько запланировано собрать?(можно не указывать)', default=0)
    current_collect = models.IntegerField('Текущая сумма сбора', default=0)
    people_donated = models.IntegerField('сколько человек сделало пожертвования', default=0)
    img_collect = models.FileField('Обложка сбора',blank=True, upload_to='media')
    last_day_collect = models.DateTimeField('Установите срок сбора', default=timezone.now)

    def __str__(self):
        return self.title