from django.db import models


class CaptureMethod(models.TextChoices):
    AUTO = 'AUTO', 'Автоматический платеж'
    MANUAL = 'MANUAL', 'Двухстадийный платеж'


class OrderStatus(models.TextChoices):
    UNPAID = 'UNPAID', 'Не оплачено'
    HOLD = 'HOLD', 'Холдированный'
    PAID = 'PAID', 'Оплачено'
