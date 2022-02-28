from os import name
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    OffersSliderListView,
    OffersSliderDetailView,

    CurrenPromotionsSliderListView,
    CurrenPromotionsSliderDetailView,
)

urlpatterns = [
    path('offers-slider/', OffersSliderListView.as_view(), name="offers-slider"),
    path('offers-slider/<slug:slug>', OffersSliderDetailView.as_view(), name='offers-slider-detail'),
    path('current-promotions-slider/', CurrenPromotionsSliderListView.as_view(), name="current-promotions-slider"),
    path('current-promotions-slider/<slug:slug>', CurrenPromotionsSliderDetailView.as_view(), name="current-promotions-slider-detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])