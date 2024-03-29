from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from django.urls import path, include
urlpatterns = [
    path('account/', include('accounts.urls')),
    path('ads/', include('ads.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)