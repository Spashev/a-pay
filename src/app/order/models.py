from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.models import TimestampMixin, UUIDMixin, Currency
from order import CaptureMethod, OrderStatus


class Order(UUIDMixin, TimestampMixin, models.Model):
    amount = models.IntegerField(verbose_name='Сумма')
    currency = models.CharField(verbose_name=_("Валюта"), choices=Currency.choices, default=Currency.KZT, max_length=6)
    capture_method = models.CharField(verbose_name='Способ списания платежа', max_length=10,
                                      choices=CaptureMethod.choices, default=CaptureMethod.AUTO)
    external_id = models.CharField(verbose_name='Внешний идентификатор заказа', max_length=100)
    description = models.CharField(verbose_name='Описание заказа', max_length=255)
    mcc = models.CharField(verbose_name='MCC Код', max_length=4, null=True, blank=True)
    extra_info = models.CharField(verbose_name='Дополнительные данные, связанные с заказом', max_length=255, null=True,
                                  blank=True)
    attempts = models.IntegerField(verbose_name='Количество попыток оплаты', default=10,
                                   validators=[MaxValueValidator(50), MinValueValidator(1)])
    customer_id = models.CharField(verbose_name='Идентификатор плательщика', max_length=10, blank=True, null=True)
    backref = models.CharField(verbose_name='Checkout url', max_length=255, null=True, blank=True)
    legal_entity = models.ForeignKey(to='legal_entity.LegalEntity', related_name='orders', on_delete=models.PROTECT)
    order_status = models.CharField(verbose_name=_("Статус заявки"), choices=OrderStatus.choices,
                                    default=OrderStatus.UNPAID, max_length=6)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        db_table = 'orders'

    def __str__(self):
        return f'{self.uuid} - {self.mcc}'
