from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import category_models
from .models import brand_models
from .serializers import (
    FirstLevelCategorySerializer, 
    SecondLevelCategorySerializer, 
    ThirdLevelCategorySerializer,
    BrandSerializer,
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


# Brand Serializer

class BrandListView(generics.ListCreateAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = brand_models.Brand.objects.all()
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]