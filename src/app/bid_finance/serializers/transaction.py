from rest_framework import serializers

from bid_finance.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        depth = 1
        fields = '__all__'
