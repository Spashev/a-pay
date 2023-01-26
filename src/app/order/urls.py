from django.urls import path
from order.views import OrderViewSet, OrderDetailViewSet


urlpatterns = [
    path('', OrderViewSet.as_view()),
    path('<uuid:uuid>', OrderDetailViewSet.as_view())
]
