from django.contrib import admin
from django.urls import path, include
from fakeapi.views import MyObtainTokenPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fakeapi.urls')),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
