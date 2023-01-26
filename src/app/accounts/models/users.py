import string
import secrets

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

from accounts import UserAccountType, RoleType
from accounts.models.managers import UserManager
from accounts.tasks import send_password_reset_notification

from utils.logger import log_exception
from utils.models import TimestampMixin


class User(
    TimestampMixin,
    AbstractUser,
    models.Model,
):
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True, )
    account_type = models.CharField(verbose_name=_("Тип аккаунта"), max_length=32, choices=UserAccountType.choices, default=UserAccountType.MANAGER,)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=15, blank=True)
    role = models.CharField(verbose_name=_("Роли"), choices=RoleType.choices, default=RoleType.LEGAL, max_length=14)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")
        db_table = 'users'

    @staticmethod
    def generate_password():
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        return password

    def reset_password(self):
        password = self.generate_password()
        self.set_password(password)
        self.save()
        self.send_mail_invitation(password)
        return password

    def send_mail_invitation(self, password: str) -> None:
        try:
            send_password_reset_notification.delay(self.email, password)
        except Exception as e:
            log_exception(e, 'Error in send_mail_invitation')
