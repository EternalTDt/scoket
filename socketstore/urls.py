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
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # accounts
    path("api/accounts/",include("accounts.urls")),
    # shop api
    path('api/shop/', include('shop.urls')),
    # mainpage api
    path('api/mainpage/', include('mainpage.urls')),
    # other info api
    path('api/services/', include('services.urls')),
    # blog api
    path('api/blog/', include('blog.urls')),
]


urlpatterns += doc_urls

