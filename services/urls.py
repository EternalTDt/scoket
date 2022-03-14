from unicodedata import name
from django.urls import path
from .views import (
    WorkingInfoListView,
    SocialLinksListView,
)


urlpatterns = [
    path('working-info/', WorkingInfoListView.as_view(), name='working-info'),
    path('social-links/', SocialLinksListView.as_view(), name='social-links')
]
