from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from src.settings.base import (
    MEDIA_URL,
    MEDIA_ROOT
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.api.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)