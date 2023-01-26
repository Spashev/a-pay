from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimestampMixin


class LegalEntityType(TimestampMixin, models.Model):
    system_name = models.CharField(verbose_name='Имя внутри системы', max_length=100)
    display_name = models.CharField(verbose_name='Имя', max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Тип юр.лиц")
        verbose_name_plural = _("Тип юр.лиц")
        db_table = 'legal_entity_type'
        unique_together = ['system_name', 'display_name']

    def __str__(self):
        return f'{self.system_name}'


class LegalEntity(TimestampMixin, models.Model):
    bin = models.CharField(verbose_name=_('БИН'), max_length=22, unique=True)
    full_name = models.CharField(verbose_name=_('Полное наименование'), max_length=255)
    short_name = models.CharField(verbose_name=_('Краткое наименование'), max_length=255)
    address = models.CharField(verbose_name=_('Адрес'), max_length=255)
    email = models.CharField(verbose_name=_('Email'), max_length=50, unique=True)
    country = models.CharField(verbose_name=_('Страна'), max_length=255, blank=True, null=True)
    editor_id = models.IntegerField(verbose_name=_('Изменил данные'), null=True, blank=True)
    kbe = models.CharField(verbose_name=_('KBE - 2 символа'), max_length=4, null=True, blank=True)
    fee_withdraw_percent = models.CharField(verbose_name=_('Комиссия для операцию в процентах'), max_length=4,
                                            null=True, blank=True)
    legal_entity_type = models.ForeignKey(to=LegalEntityType, related_name='type', verbose_name='Тип юр.лиц',
                                          on_delete=models.PROTECT)
    legal_entity_config = models.ForeignKey(to='LegalEntityConfig', related_name='core', verbose_name='Конфиг',
                                            on_delete=models.PROTECT, blank=True, null=True)
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='legal_entity', verbose_name='Пользователь',
                                on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Мерчант")
        verbose_name_plural = _("Мерчанты")
        db_table = 'legal_entity'
        unique_together = ['bin', 'email']

    def __str__(self):
        return f'{self.full_name} - {self.bin}'
