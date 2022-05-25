from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_multiple_model.views import FlatMultipleModelAPIView, ObjectMultipleModelAPIView

from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models
from .service import (
    SocketFilter,
    SwitchFilter,
    FrameFilter,
    PlugFilter,
    ComputerSocketFilter,
    DimmerFilter,
    ThermostatFilter,
    NetworkFilterFilter,
)

from .serializers import (
    FirstLevelCategorySerializer, 
    SecondLevelCategorySerializer, 
    ThirdLevelCategorySerializer,

    BrandSerializer,

    CollectionSerializer,
    CollectionOfferSerializer,

    ProductOfferSerializer,

    SocketSerializer,
    SwitchSerializer,
    FrameSerializer,
    PlugSerializer,
    ComputerSocketSerializer,
    DimmerSerializer,
    ThermostatSerializer,
    NetworkFilterSerializer,
)


#  FirstLevelCategory


class FirstLevelCategoryListView(generics.ListAPIView):
    queryset = category_models.FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FirstLevelCategoryDetailView(generics.RetrieveAPIView):
    queryset = category_models.FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# SecondLevelCategory


class SecondLevelCategoryListView(generics.ListAPIView):
    queryset = category_models.SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SecondLevelCategoryDetailView(generics.RetrieveAPIView):
    queryset = category_models.SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# ThirdLevelCategory


class ThirdLevelCategoryListView(generics.ListAPIView):
    queryset = category_models.ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ThirdLevelCategoryDetailView(generics.RetrieveAPIView):
    queryset = category_models.ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Brand

class BrandListView(generics.ListAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class BrandDetailView(generics.RetrieveAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Collection

class CollectionListView(generics.ListAPIView):
    queryset = collection_models.Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class CollectionDetailView(generics.RetrieveAPIView):
    queryset = collection_models.Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Collection offer

class CollectionOfferListView(generics.ListAPIView):
    queryset = collection_models.CollectionOffer.objects.all()
    serializer_class = CollectionOfferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CollectionOfferDetailView(generics.RetrieveAPIView):
    queryset = collection_models.CollectionOffer.objects.all()
    serializer_class = CollectionOfferSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Product offer

class ProductOfferListView(generics.ListAPIView):
    queryset = product_models.ProductOffer.objects.all()
    serializer_class = ProductOfferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] 


class ProductOfferDetailView(generics.RetrieveAPIView):
    queryset = product_models.ProductOffer.objects.all()
    serializer_class = ProductOfferSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductsAPIView(FlatMultipleModelAPIView):
    querylist = [
        {
            'queryset': product_models.Socket.objects.all(), 
            'serializer_class': SocketSerializer, 
            'label': 'socket',
        },
        {
            'queryset': product_models.Switch.objects.all(), 
            'serializer_class': SwitchSerializer,
            'label': 'switch',
        },
        {
            'queryset': product_models.Frame.objects.all(), 
            'serializer_class': FrameSerializer,
            'label': 'frame',
        },
        {
            'queryset': product_models.Plug.objects.all(), 
            'serializer_class': PlugSerializer,
            'label': 'plug',
        },
        {
            'queryset': product_models.ComputerSocket.objects.all(), 
            'serializer_class': ComputerSocketSerializer,
            'label': 'computer-socket',
        },
        {
            'queryset': product_models.Dimmer.objects.all(), 
            'serializer_class': DimmerSerializer,
            'label': 'dimmer',
        },
        {
            'queryset': product_models.Thermostat.objects.all(), 
            'serializer_class': ThermostatSerializer,
            'label': 'thermostat',
        },
        {
            'queryset': product_models.NetworkFilter.objects.all(), 
            'serializer_class': NetworkFilterSerializer,
            'label': 'network-filter',
        },
    ]


# Socket

class SocketListView(generics.ListAPIView):
    queryset = product_models.Socket.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SocketFilter
    serializer_class = SocketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class SocketDetailView(generics.RetrieveAPIView):
    queryset = product_models.Socket.objects.all()
    serializer_class = SocketSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Switch

class SwitchListView(generics.ListAPIView):
    queryset = product_models.Switch.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SwitchFilter
    serializer_class = SwitchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class SwitchDetailView(generics.RetrieveAPIView):
    queryset = product_models.Switch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Frame

class FrameListView(generics.ListAPIView):
    queryset = product_models.Frame.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = FrameFilter
    serializer_class = FrameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class FrameDetailView(generics.RetrieveAPIView):
    queryset = product_models.Frame.objects.all()
    serializer_class = FrameSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Plug

class PlugListView(generics.ListAPIView):
    queryset = product_models.Plug.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlugFilter
    serializer_class = PlugSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class PlugDetailView(generics.RetrieveAPIView):
    queryset = product_models.Plug.objects.all()
    serializer_class = PlugSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Computer Socket

class ComputerSocketListView(generics.ListAPIView):
    queryset = product_models.ComputerSocket.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ComputerSocketFilter
    serializer_class = ComputerSocketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class ComputerSocketDetailView(generics.RetrieveAPIView):
    queryset = product_models.ComputerSocket.objects.all()
    serializer_class = ComputerSocketSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Dimmer

class DimmerListView(generics.ListAPIView):
    queryset = product_models.Dimmer.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DimmerFilter
    serializer_class = DimmerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class DimmerDetailView(generics.RetrieveAPIView):
    queryset = product_models.Dimmer.objects.all()
    serializer_class = DimmerSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Thermostat

class ThermostatListView(generics.ListAPIView):
    queryset = product_models.Thermostat.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ThermostatFilter
    serializer_class = ThermostatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class ThermostatDetailView(generics.RetrieveAPIView):
    queryset = product_models.Thermostat.objects.all()
    serializer_class = ThermostatSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Network Filter

class NetworkFilterListView(generics.ListAPIView):
    queryset = product_models.NetworkFilter.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NetworkFilterFilter
    serializer_class = NetworkFilterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class NetworkFilterDetailView(generics.RetrieveAPIView):
    queryset = product_models.NetworkFilter.objects.all()
    serializer_class = NetworkFilterSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
