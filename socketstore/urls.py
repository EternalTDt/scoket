from django.conf import settings
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .yasg import urlpatterns as doc_urls


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
	# djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # accounts
    path('accounts/api/',include("accounts.urls")),
    # shop api
    path('api/shop/', include('shop.urls')),
    # other info api
    path('services/api/', include('services.urls')),
    # blog api
    path('blog/api/', include('blog.urls')),
    # orders
    path('orders/api/', include('orders.urls')),
]


urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
