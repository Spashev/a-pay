from rest_framework import serializers

from bank.models import Bank


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = (
            'id',
            'name',
            'bin',
            'bik',
        )
