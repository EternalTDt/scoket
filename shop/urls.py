from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    FirstLevelCategoryListView, 
    FirstLevelCategoryDetailView,

    SecondLevelCategoryListView, 
    SecondLevelCategoryDetailView,

    ThirdLevelCategoryListView,
    ThirdLevelCategoryDetailView,

    BrandListView,
    BrandDetailView,

    CollectionListView,
    CollectionDetailView,

    CollectionOfferListView,
    CollectionOfferDetailView,

    SocketListView,
    SocketDetailView,

    SwitchListView,
    SwitchDetailView,

    FrameListView,
    FrameDetailView,

    PlugListView,
    PlugDetailView,

    ComputerSocketListView,
    ComputerSocketDetailView,

    DimmerListView,
    DimmerDetailView,

    ThermostatListView,
    ThermostatDetailView,

    NetworkFilterListView,
    NetworkFilterDetailView,

)

urlpatterns = [
    path('first-level-categories/', FirstLevelCategoryListView.as_view(), name='first-level-categories'),
    path('first-level-categories/<slug:slug>/', FirstLevelCategoryDetailView.as_view(), name='first-level-categories-detail'),
    path('second-level-categories/', SecondLevelCategoryListView.as_view(), name='second-level-categories'),
    path('second-level-categories/<slug:slug>/', SecondLevelCategoryDetailView.as_view(), name='second-level-categories-detail'),
    path('third-level-categories/', ThirdLevelCategoryListView.as_view(), name='third-level-categories'),
    path('third-level-categories/<slug:slug>/', ThirdLevelCategoryDetailView.as_view(), name='third-level-categories-detail'),
    path('brand/', BrandListView.as_view(), name='brand'),
    path('brand/<slug:slug>/', BrandDetailView.as_view(), name='brand-detail'),
    path('collection/', CollectionListView.as_view(), name='collection'),
    path('collection/<slug:slug>/', CollectionDetailView.as_view(), name='collection-detail'),
    path('collection-offer/', CollectionOfferListView.as_view(), name='collection-offer'),
    path('collection-offer/<slug:slug>/', CollectionOfferDetailView.as_view(), name='collection-offer-detail'),
    path('product/socket/', SocketListView.as_view(), name="socket"),
    path('product/socket/<slug:slug>/', SocketDetailView.as_view(), name="socket-detail"),
    path('product/switch/', SwitchListView.as_view(), name="switch"),
    path('product/switch/<slug:slug>/', SwitchDetailView.as_view(), name="switch-detail"),
    path('product/frame/', FrameListView.as_view(), name="frame"),
    path('product/frame/<slug:slug>/', FrameDetailView.as_view(), name="frame-detail"),
    path('product/plug/', PlugListView.as_view(), name="plug"),
    path('product/plug/<slug:slug>/', PlugDetailView.as_view(), name="plug-detail"),
    path('product/computer-socket/', ComputerSocketListView.as_view(), name="computer-socket"),
    path('product/computer-socket/<slug:slug>/', ComputerSocketDetailView.as_view(), name="computer-socket-detail"),
    path('product/dimmer/', DimmerListView.as_view(), name="dimmer"),
    path('product/dimmer/<slug:slug>/', DimmerDetailView.as_view(), name="dimmer-detail"),
    path('product/thermostat/', ThermostatListView.as_view(), name="thermostat"),
    path('product/thermostat/<slug:slug>/', ThermostatDetailView.as_view(), name="thermostat-detail"),
    path('product/network-filter/', NetworkFilterListView.as_view(), name="network-filter"),
    path('product/network-filter/<slug:slug>/', NetworkFilterDetailView.as_view(), name="network-filter-detail"),
]

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])