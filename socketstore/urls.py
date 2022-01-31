from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/', include('fakeapi.urls')),
    # path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
