from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from core.swagger import swagger_patterns
from bid_finance.views import TemplateDetailViewSet

urlpatterns = [
    path('swagger/', include(swagger_patterns)),

    path('admin/', admin.site.urls),
    path('api/users/', include('accounts.urls')),
    path('api/', include('legal_entity.urls')),
    path('api/', include('bid_finance.urls')),
    path('api/orders/', include('order.urls')),
    path('api/banks/', include('bank.urls')),
    path('3ds/<uuid:uuid>', TemplateDetailViewSet.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
