from django.db.models import TextChoices


class TransactionType(TextChoices):
    INIT_PAYMENT = 'INIT_PAYMENT'
    APPROVE = 'APPROVE'
    CAPTURE = 'CAPTURE'
    CANCEL = 'CANCEL'
    REFUND = 'REFUND'
    FINISH_3D_SECURE = 'FINISH_3D_SECURE'
    GET_STATUS = 'GET_STATUS'


class TransactionStatus(TextChoices):
    SUCCEEDED = 'SUCCEEDED', 'Успешный'
    PROCESSING = 'PROCESSING', 'В обработке'
    FAILED = 'FAILED', 'Неуспешный'


class BidFinanceStatus(TextChoices):
    CAPTURED = 'CAPTURED', 'Зарегистрированная'
    APPROVED = 'APPROVED', 'Одобренный'
    PROCESSING = 'PROCESSING', 'В обработке'
    FAILED = 'FAILED', 'Неуспешный'
    CANCELLED = 'CANCELLED', 'Отмененный'
    REFUNDED = 'REFUNDED', 'Возврат'


class BidFinanceType(TextChoices):
    PAYMENT = 'PAYMENT', 'Платеж'
    TRANSFER = 'TRANSFER', 'Перевод'
