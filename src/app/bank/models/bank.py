from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimestampMixin


class Bank(TimestampMixin, models.Model):
    name = models.CharField(verbose_name='Наименование банка', max_length=64)
    bin = models.CharField(verbose_name='БИН', max_length=22)
    bik = models.CharField(verbose_name='БИК', max_length=22)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Банк")
        verbose_name_plural = _("Список банков")
        db_table = 'bank'

    def __str__(self):
        return f'{self.name} - {self.bin}'
