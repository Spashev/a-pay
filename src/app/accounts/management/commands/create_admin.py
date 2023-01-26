from accounts.models import User
from accounts import RoleType, UserAccountType
from django.core.management.base import BaseCommand

from legal_entity.models import LegalEntity, LegalEntityType


class Command(BaseCommand):
    help = 'Create admin user'

    def handle(self, *args, **kwargs):
        user: User = User.objects.create_superuser(
            username='root',
            first_name="Asadalpay",
            last_name="A-pay",
            email="asadalpay@asadalpay.com",
            role=RoleType.ADMINISTRATIVE,
            password='123',
            account_type=UserAccountType.ADMIN
        )
        LegalEntityType.objects.create(
            system_name='TOO',
            display_name="TOO"
        )
        LegalEntityType.objects.create(
            system_name='AO',
            display_name="AO"
        )
        LegalEntity.objects.create(
            user_id=user.id,
            bin='1234567890',
            full_name="TOO Asadalpay",
            short_name="A-pay",
            address='Алматы, Сайна 30',
            email="asadalpay@asadalpay.com",
            editor_id=1,
            kbe='1234',
            fee_withdraw_percent=3,
            legal_entity_type_id=1
        )
