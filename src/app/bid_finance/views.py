from rest_framework import generics, views, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from bid_finance.models import BidFinance, Transaction, Template
from bid_finance.serializers import (
    BidFinanceSerializer,
    TransactionSerializer
)
from utils.services import get_domain

from django.views.generic.base import TemplateView


class BidFinanceViewSet(generics.ListAPIView):
    model = BidFinance
    queryset = BidFinance.objects.all()
    serializer_class = BidFinanceSerializer


class BidFinanceDetailViewSet(views.APIView):
    model = BidFinance

    def get(self, request, uuid):
        bid_finance = BidFinance.objects.get(uuid=uuid)
        bid_finance_serializer = BidFinanceSerializer(bid_finance)

        return Response(bid_finance_serializer.data)


class TransactionViewSet(generics.ListAPIView):
    model = Transaction
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class TemplateDetailViewSet(TemplateView):
    model = Template
    template_name = '3ds/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bid_finance = get_object_or_404(BidFinance, uuid=kwargs.get('uuid'))
        template = Template.objects.get(bid_finance_id=bid_finance.id)
        context['template'] = template

        return context


class TemplateLinkViewSet(views.APIView):
    model = Template

    def get(self, request, uuid):
        bid_finance = BidFinance.objects.filter(uuid=uuid).first()
        if bid_finance is None:
            return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        template = bid_finance.template
        if template:
            domain = get_domain(request)
            return Response({'link': f'{domain}/3ds/{uuid}'}, status=status.HTTP_200_OK)
        return Response({'message': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
