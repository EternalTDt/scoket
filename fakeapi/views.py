from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
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
    permission_classes = [IsAuthenticated]


class FirstLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


# SecondLevelCategory


class SecondLevelCategoryListView(generics.ListCreateAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    permission_classes = [IsAuthenticated]


class SecondLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


# ThirdLevelCategory


class ThirdLevelCategoryListView(generics.ListCreateAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    permission_classes = [IsAuthenticated]


class ThirdLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]


# Brand Serializer

class BrandListView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_classe = BrandSerializer
    permission_classes = [IsAuthenticated]


class BrandDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_classe = BrandSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]