from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Collect(models.Model):

    author_collect = models.ForeignKey(
        User, on_delete=models.PROTECT,
        verbose_name='Автор сбора'
    )

    title = models.CharField('Название', max_length=200)

    reason = models.CharField(
        'Повод для сбора',
        max_length=64,
    )

    description = models.TextField(
        'Описание',
        max_length=600,
        blank=True
    )

    goal_collect = models.IntegerField(
        'Сколько запланировано собрать?(можно не указывать)',
        default=0
    )

    img_collect = models.FileField(
        'Обложка сбора',
        blank=True,
        null=True,
        upload_to='media'
    )

    last_day_collect = models.DateTimeField(
        'Установите срок сбора',
        default=timezone.now)

    list_donation = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Collect"
        verbose_name_plural = "Collects"
        unique_together = [["author_collect", "title"]]
