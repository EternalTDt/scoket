from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import LimitOffsetPagination

from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models

from .serializers import (
    FirstLevelCategorySerializer, 
    SecondLevelCategorySerializer, 
    ThirdLevelCategorySerializer,

    BrandSerializer,

    CollectionSerializer,
    CollectionOfferSerializer,

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


class FirstLevelCategoryListView(generics.ListCreateAPIView):
    queryset = category_models.FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FirstLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = category_models.FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# SecondLevelCategory


class SecondLevelCategoryListView(generics.ListCreateAPIView):
    queryset = category_models.SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SecondLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = category_models.SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# ThirdLevelCategory


class ThirdLevelCategoryListView(generics.ListCreateAPIView):
    queryset = category_models.ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ThirdLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = category_models.ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Brand

class BrandListView(generics.ListCreateAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Collection

class CollectionListView(generics.ListCreateAPIView):
    queryset = collection_models.Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class CollectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = collection_models.Collection.objects.all()
    serializer_class = CollectionSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Collection offer

class CollectionOfferListView(generics.ListCreateAPIView):
    queryset = collection_models.CollectionOffer.objects.all()
    serializer_class = CollectionOfferSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CollectionOfferDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = collection_models.CollectionOffer.objects.all()
    serializer_class = CollectionOfferSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Socket

class SocketListView(generics.ListCreateAPIView):
    queryset = product_models.Socket.objects.all()
    serializer_class = SocketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class SocketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Socket.objects.all()
    serializer_class = SocketSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Switch

class SwitchListView(generics.ListCreateAPIView):
    queryset = product_models.Switch.objects.all()
    serializer_class = SwitchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class SwitchDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Switch.objects.all()
    serializer_class = SwitchSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Frame

class FrameListView(generics.ListCreateAPIView):
    queryset = product_models.Frame.objects.all()
    serializer_class = FrameSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class FrameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Frame.objects.all()
    serializer_class = FrameSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Plug

class PlugListView(generics.ListCreateAPIView):
    queryset = product_models.Plug.objects.all()
    serializer_class = PlugSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class PlugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Plug.objects.all()
    serializer_class = PlugSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Computer Socket

class ComputerSocketListView(generics.ListCreateAPIView):
    queryset = product_models.ComputerSocket.objects.all()
    serializer_class = ComputerSocketSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class ComputerSocketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.ComputerSocket.objects.all()
    serializer_class = ComputerSocketSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Dimmer

class DimmerListView(generics.ListCreateAPIView):
    queryset = product_models.Dimmer.objects.all()
    serializer_class = DimmerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class DimmerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Dimmer.objects.all()
    serializer_class = DimmerSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Thermostat

class ThermostatListView(generics.ListCreateAPIView):
    queryset = product_models.Thermostat.objects.all()
    serializer_class = ThermostatSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class ThermostatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.Thermostat.objects.all()
    serializer_class = ThermostatSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Network Filter

class NetworkFilterListView(generics.ListCreateAPIView):
    queryset = product_models.NetworkFilter.objects.all()
    serializer_class = NetworkFilterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination


class NetworkFilterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product_models.NetworkFilter.objects.all()
    serializer_class = NetworkFilterSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
