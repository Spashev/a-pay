from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimestampMixin


class LegalEntityConfig(TimestampMixin, models.Model):
    legal_entity = models.ForeignKey(to='legal_entity.LegalEntity', verbose_name='Юр.лицо', on_delete=models.CASCADE)
    terminal = models.CharField(verbose_name='Терминал', max_length=100)
    merchant_name = models.CharField(verbose_name='Название мерчанта', max_length=255)
    merchant_url = models.URLField(verbose_name='Мерчант url', max_length=255, null=True, blank=True)
    notify_url = models.URLField(verbose_name='Мерчант notify url', max_length=255, null=True, blank=True)
    merchant_gtm = models.CharField(verbose_name='GTM+', max_length=255, null=True, blank=True)
    nonce = models.CharField(verbose_name='Nonce', max_length=255, null=True, blank=True)
    p_sign = models.CharField(verbose_name='P_SIGN', max_length=255, blank=True, null=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Конфиг мерчанта")
        verbose_name_plural = _("Конфиги мерчанта")
        db_table = 'legal_entity_config'

    def __str__(self):
        return f'{self.legal_entity} - {self.terminal}'
