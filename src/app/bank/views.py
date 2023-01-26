from rest_framework import mixins, viewsets

from bank.models import Bank
from bank.serializers import BankSerializer


class BankViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
