from rest_framework import serializers

from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    bid_finance = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            'uuid',
            'amount',
            'currency',
            'capture_method',
            'external_id',
            'description',
            'mcc',
            'extra_info',
            'attempts',
            'customer_id',
            'bid_finance'
        )
