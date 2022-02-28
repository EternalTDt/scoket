from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api/shop/', include('shop.urls')),
    path('api/mainpage/', include('mainpage.urls')),
]


urlpatterns += doc_urls

