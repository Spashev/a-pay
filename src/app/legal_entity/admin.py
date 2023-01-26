from django.contrib import admin
from legal_entity.models import LegalEntity, LegalEntityConfig, LegalEntityType


admin.site.register(LegalEntity)
admin.site.register(LegalEntityType)
admin.site.register(LegalEntityConfig)
