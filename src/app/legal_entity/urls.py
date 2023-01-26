from django.urls import path, include

from rest_framework.routers import DefaultRouter

from legal_entity.views import LegalEntityViewSet, LegalEntityTypeViewSet, LegalEntityConfigViewSet


router = DefaultRouter(trailing_slash=True)
router.register('legal-entity', LegalEntityViewSet, basename='legal-entity')
router.register('legal-entity-type', LegalEntityTypeViewSet, basename='legal-entity-type')
router.register('legal-entity-config', LegalEntityConfigViewSet, basename='legal-entity-config')


urlpatterns = [
    path('', include(router.urls)),
]
