from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import UUIDMixin, TimestampMixin, Currency
from bid_finance import BidFinanceStatus, BidFinanceType


class BidFinanceTye(TimestampMixin, models.Model):
    system_name = models.CharField(verbose_name='Имя внутри системы', max_length=100)
    display_name = models.CharField(verbose_name='Имя', max_length=100)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Тип финансовых операция")
        verbose_name_plural = _("Тип финансовых операции")
        db_table = 'bid_finance_type'
        unique_together = ['system_name', 'display_name']

    def __str__(self):
        return f'{self.system_name}'


class BidFinance(UUIDMixin, TimestampMixin, models.Model):
    initiator = models.ForeignKey(to='legal_entity.LegalEntity', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(verbose_name=_('Сумма'))
    total_amount = models.IntegerField(verbose_name=_('Общая сумма заявки, включая коммисии'))
    reversed_at = models.DateTimeField(verbose_name=_('Дата сторнирования'), auto_now=True, null=True, blank=True)
    description = models.CharField(verbose_name=_('Описание (причина отклонения, описание ошибки, причинасторно)'),
                                   max_length=255, null=True, blank=True)
    original_bid_id = models.IntegerField(verbose_name=_('ID исходной заявки (для заявок “Сторно”)'), null=True,
                                          blank=True)
    receiver_phone = models.CharField(verbose_name=_('Tелефон получателя'),
                                      max_length=64, null=True, blank=True)
    api_id = models.CharField(verbose_name=_('API с которого была созадана заявка'), max_length=22, null=True,
                              blank=True)
    fee_merchant_sent = models.DecimalField(verbose_name=_('Сумма комиссии, списанная с Мерчанта'), max_digits=14,
                                            decimal_places=2, null=True, blank=True)
    fee_merchant_received = models.DecimalField(verbose_name=_('Сумма комиссии, полученная Мерчантом'), max_digits=14,
                                                decimal_places=2, null=True, blank=True)
    bid_finance_status = models.CharField(verbose_name=_("Статус операция"), choices=BidFinanceStatus.choices,
                                          default=BidFinanceStatus.PROCESSING, max_length=20)

    bid_finance_type = models.CharField(verbose_name=_('Тип финансовой операции'), choices=BidFinanceType.choices,
                                        max_length=20)
    currency = models.CharField(verbose_name=_("Валюта"), choices=Currency.choices, default=Currency.KZT, max_length=6)
    order = models.ForeignKey(to='order.Order', verbose_name='Заказ', on_delete=models.PROTECT,
                              related_name='bid_finances')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Финансовая операция")
        verbose_name_plural = _("Финансовые операции")
        db_table = 'bid_finance'
        index_together = [
            ["uuid"],
        ]

    def __str__(self):
        return f'{self.initiator} - {self.uuid}'


class Template(TimestampMixin, models.Model):
    origin_template = models.TextField(verbose_name='Шаблон формы оплаты', blank=True, null=True)
    updated_template = models.TextField(verbose_name='Шаблон формы оплаты', blank=True, null=True)
    bid_finance = models.OneToOneField(verbose_name='Заказ', to=BidFinance, blank=True, null=True,
                                       on_delete=models.CASCADE, related_name='template')

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Шаблон")
        verbose_name_plural = _("Шаблоны")
        db_table = 'templates'

    def __str__(self):
        return f'Template {self.id}'
