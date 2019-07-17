from django.conf.urls.static import static
from django.conf import settings
from django.apps import apps
from django.urls import include, path  # > Django-2.0
from django.contrib import admin

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # > Django-2.0
    path('admin/', admin.site.urls),  # > Django-2.0
    path('', include(apps.get_app_config('oscar').urls[0])),  # > Django-2.0
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)