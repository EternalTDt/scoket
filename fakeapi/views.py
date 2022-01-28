from rest_framework import generics
from .models import (
    FirstLevelCategory, 
    SecondLevelCategory,
    ThirdLevelCategory,
    Brand,
)
from .serializers import (
    FirstLevelCategorySerializer, 
    SecondLevelCategorySerializer, 
    ThirdLevelCategorySerializer,
    BrandSerializer,
)


#  FirstLevelCategory


class FirstLevelCategoryListView(generics.ListCreateAPIView):
    queryset = FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer


class FirstLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    lookup_field = 'slug'


# SecondLevelCategory


class SecondLevelCategoryListView(generics.ListCreateAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer


class SecondLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    lookup_field = 'slug'


# ThirdLevelCategory


class ThirdLevelCategoryListView(generics.ListCreateAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer


class ThirdLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    lookup_field = 'slug'


# Brand Serializer

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_classe = BrandSerializer


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_classe = BrandSerializer
    lookup_field = 'slug'