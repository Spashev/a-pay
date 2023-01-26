from rest_framework import generics, views
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer


class OrderViewSet(generics.ListAPIView):
    model = Order
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewSet(views.APIView):
    model = Order

    def get(self, request, uuid):
        order = Order.objects.get(uuid=uuid)
        order_serializer = OrderSerializer(order)

        return Response(order_serializer.data)
