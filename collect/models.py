from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from collect.tasks import send_collect_notification



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
    img_collect = models.FileField('Обложка сбора',blank=True, null=True, upload_to='media')
    last_day_collect = models.DateTimeField('Установите срок сбора', default=timezone.now)
    list_donation = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, save_model=True, **kwargs):
        if save_model:
            send_collect_notification.delay(
                self.author_collect.first_name,
                self.title,
                self.author_collect.email
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
