from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fakeapi.urls')),
    path('auth/', include('auth.urls')),
    # path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
