from django.urls import path, include
from rest_framework.routers import DefaultRouter

from bank.views import BankViewSet


router = DefaultRouter(trailing_slash=True)
router.register('', BankViewSet, basename='bank')

urlpatterns = [
    path('', include(router.urls))
]
