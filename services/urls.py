from django.urls import path
from .views import (
    WorkingInfoListView,
    SocialLinksListView,
    MailSubscriptionAPIView,
)


urlpatterns = [
    path('working-info/', WorkingInfoListView.as_view(), name='working-info'),
    path('social-links/', SocialLinksListView.as_view(), name='social-links'),
    path('subscribe-email/', MailSubscriptionAPIView.as_view(), name='subscribe-email'),
]
