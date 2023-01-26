from django.db import transaction
from rest_framework import serializers

from bid_finance.models import BidFinance, Template
from bid_finance.serializers.transaction import TransactionSerializer


class BidFinanceSerializer(serializers.ModelSerializer):
    transactions = TransactionSerializer(read_only=True, many=True)

    class Meta:
        model = BidFinance
        depth = 1
        fields = (
            'id',
            'uuid',
            'initiator',
            'amount',
            'total_amount',
            'reversed_at',
            'description',
            'original_bid_id',
            'receiver_phone',
            'api_id',
            'fee_merchant_sent',
            'fee_merchant_received',
            'bid_finance_status',
            'bid_finance_type',
            'currency',
            'transactions',
        )

        @transaction.atomic
        def create(self, validated_data):
            instance: BidFinance = BidFinance.objects.create_user(**validated_data)
            return instance


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
