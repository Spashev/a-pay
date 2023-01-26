from django.urls import path
from bid_finance.views import BidFinanceViewSet, TransactionViewSet, BidFinanceDetailViewSet, TemplateLinkViewSet


urlpatterns = [
    path('bid-finance/', BidFinanceViewSet.as_view()),
    path('bid-finance/transactions', TransactionViewSet.as_view()),
    path('bid-finance/<uuid:uuid>', BidFinanceDetailViewSet.as_view()),
    path('template/<uuid:uuid>', TemplateLinkViewSet.as_view()),
]
