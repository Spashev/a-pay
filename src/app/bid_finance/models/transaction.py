from django.db import models
from django.utils.translation import gettext_lazy as _

from bid_finance import TransactionStatus, TransactionType

from utils.models import TimestampMixin, Currency


class Transaction(TimestampMixin, models.Model):
    amount = models.IntegerField(verbose_name='сумма')
    bid_finance = models.ForeignKey(to='bid_finance.BidFinance', related_name='transactions',
                                    verbose_name='ID фин. заявки',
                                    on_delete=models.PROTECT)
    currency = models.CharField(verbose_name=_("Валюта"), choices=Currency.choices, default=Currency.KZT, max_length=6)
    transaction_status = models.CharField(verbose_name=_("Статус транзакции"), choices=TransactionStatus.choices,
                                          max_length=10)
    transaction_type = models.CharField(verbose_name=_("Тип транзакции"), choices=TransactionType.choices,
                                        default=TransactionType.INIT_PAYMENT, max_length=30)
    sender_phone = models.CharField(verbose_name=_('Tелефон отправителя'),
                                    max_length=64, null=True, blank=True)
    receiver_phone = models.CharField(verbose_name=_('Tелефон получателяы'),
                                      max_length=64, null=True, blank=True)
    is_fee = models.BooleanField(verbose_name='Kомиссионая транзакция', default=False)
    is_reversal = models.BooleanField(verbose_name='Tранзакция сторнирования', default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Tранзакции по фин. операции")
        verbose_name_plural = _("Tранзакции по фин. операции")
        db_table = 'transaction'
        index_together = [
            ["bid_finance"],
        ]

    def __str__(self):
        return f'{self.bid_finance} - {self.amount}'
