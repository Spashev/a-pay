from rest_framework import viewsets, mixins

from legal_entity.models import (
    LegalEntity,
    LegalEntityType,
    LegalEntityConfig
)
from legal_entity.serializers import (
    LegalEntitySerializer,
    LegalEntityTypeSerializer,
    LegalEntityConfigSerializer,
    LegalEntityCreateUpdateSerializer
)


class LegalEntityViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LegalEntity.objects.all()
    serializer_class = LegalEntitySerializer

    def get_serializer_class(self):
        serializer = self.serializer_class

        if self.action == 'create':
            serializer = LegalEntityCreateUpdateSerializer
        elif self.action == 'update':
            serializer = LegalEntityCreateUpdateSerializer

        return serializer


class LegalEntityTypeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = LegalEntityType.objects.all()
    serializer_class = LegalEntityTypeSerializer


class LegalEntityConfigViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    http_method_names = ["get", "post", "put", "patch", "delete"]
    queryset = LegalEntityConfig.objects.all()
    serializer_class = LegalEntityConfigSerializer
