from django.db.models import Q
from django.db import transaction

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from accounts.models import User
from legal_entity.serializers import LegalEntitySerializer


class ListUserSerializer(serializers.ModelSerializer):
    legal_entity = LegalEntitySerializer(read_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'account_type',
            'is_active',
            'role',
            'legal_entity'
        )


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'password'
        )

    @transaction.atomic
    def create(self, validated_data):
        instance: User = User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password'),
            username=validated_data.get('username'),
        )
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'account_type',
            'is_active',
            'role'
        )

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.account_type = validated_data.get('account_type', instance.account_type)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.role_id = validated_data.get('role', instance.role)
        instance.save()

        return instance


class ResetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        if instance := User.objects.filter(Q(username=username) | Q(email=username)).first():
            attrs['instance'] = instance
            return attrs
        raise ValidationError({'username': 'User with given login/email does not exist'})

    def save(self, **kwargs):
        instance: User = self.validated_data.get('instance')
        instance.reset_password()
        return instance
