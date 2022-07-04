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

    ProductOfferListView,
    ProductOfferDetailView,

    ProductsAPIView,

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

    SocketReviewListView,

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
    path('product-offer/', ProductOfferListView.as_view(), name='product-offer'),
    path('product-offer/<slug:slug>/', ProductOfferDetailView.as_view(), name='product-offer-detail'),
]

urlpatterns_product = [
    path('products/', ProductsAPIView.as_view(), name="products"),
    path('socket/', SocketListView.as_view(), name="socket"),
    path('socket/<slug:slug>/', SocketDetailView.as_view(), name="socket-detail"),
    path('add-review/socket/', SocketReviewListView.as_view(), name='socket-add-review'),
    path('switch/', SwitchListView.as_view(), name="switch"),
    path('switch/<slug:slug>/', SwitchDetailView.as_view(), name="switch-detail"),
    path('frame/', FrameListView.as_view(), name="frame"),
    path('frame/<slug:slug>/', FrameDetailView.as_view(), name="frame-detail"),
    path('plug/', PlugListView.as_view(), name="plug"),
    path('plug/<slug:slug>/', PlugDetailView.as_view(), name="plug-detail"),
    path('computer-socket/', ComputerSocketListView.as_view(), name="computer-socket"),
    path('computer-socket/<slug:slug>/', ComputerSocketDetailView.as_view(), name="computer-socket-detail"),
    path('dimmer/', DimmerListView.as_view(), name="dimmer"),
    path('dimmer/<slug:slug>/', DimmerDetailView.as_view(), name="dimmer-detail"),
    path('thermostat/', ThermostatListView.as_view(), name="thermostat"),
    path('thermostat/<slug:slug>/', ThermostatDetailView.as_view(), name="thermostat-detail"),
    path('network-filter/', NetworkFilterListView.as_view(), name="network-filter"),
    path('network-filter/<slug:slug>/', NetworkFilterDetailView.as_view(), name="network-filter-detail"),
]

urlpatterns += urlpatterns_product

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])