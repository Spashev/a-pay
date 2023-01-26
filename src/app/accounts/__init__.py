from django.db.models import TextChoices


class UserAccountType(TextChoices):
    ADMIN = 'ADMIN', 'Админ'
    MANAGER = 'MANAGER', 'Менеджер'


class RoleType(TextChoices):
    ADMINISTRATIVE = 'ADMINISTRATIVE', 'Администратор портала'
    FINANCE = 'FINANCE', 'Финансовый отдел'
    PURCHASE = 'PURCHASE', 'Отдел закупок'
    LEGAL = 'LEGAL', 'Юридический отдел'
    DIRECTOR = 'DIRECTOR', 'Директор'
    MANAGER = 'MANAGER', 'Менеджер'
