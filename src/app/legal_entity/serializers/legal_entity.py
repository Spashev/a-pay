from rest_framework import serializers
from django.db import transaction

from legal_entity.models import LegalEntity, LegalEntityType, LegalEntityConfig
from utils.serializers import UserSerializer
from accounts.models import User


class LegalEntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntityType
        fields = '__all__'


class LegalEntityConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalEntityConfig
        fields = '__all__'


class LegalEntitySerializer(serializers.ModelSerializer):
    legal_entity_type = LegalEntityTypeSerializer(read_only=True)
    legal_entity_config = LegalEntityConfigSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = LegalEntity
        fields = (
            'id',
            'bin',
            'full_name',
            'address',
            'email',
            'editor_id',
            'kbe',
            'fee_withdraw_percent',
            'legal_entity_type',
            'legal_entity_config',
            'user',
            'created_at'
        )


class LegalEntityCreateUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    phone_number = serializers.CharField(source='user.phone_number')
    password = serializers.CharField(source='user.password')

    class Meta:
        model = LegalEntity
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'password',
            'bin',
            'full_name',
            'short_name',
            'address',
            'editor_id',
            'kbe',
            'fee_withdraw_percent',
            'legal_entity_type',
        )

    @transaction.atomic
    def create(self, validated_data):
        user: User = User.objects.create_user(
            **validated_data['user']
        )
        LegalEntity.objects.create(
            user_id=user.id,
            bin=validated_data.get('bin'),
            full_name=validated_data.get('full_name'),
            short_name=validated_data.get('short_name'),
            address=validated_data.get('address'),
            email=user.email,
            editor_id=validated_data.get('editor_id'),
            kbe=validated_data.get('kbe'),
            fee_withdraw_percent=validated_data.get('fee_withdraw_percent'),
            legal_entity_type=validated_data.get('legal_entity_type')
        )

        return validated_data
