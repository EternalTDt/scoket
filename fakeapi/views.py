from rest_framework import generics
from .models import (
    FirstLevelCategory, 
    SecondLevelCategory,
    ThirdLevelCategory
)
from .serializers import (
    FirstLevelCategorySerializer, 
    SecondLevelCategorySerializer, 
    ThirdLevelCategorySerializer
)


#  FirstLevelCategory


class FirstLevelCategoryListView(generics.ListCreateAPIView):
    queryset = FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer


class FirstLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FirstLevelCategory.objects.all()
    serializer_class = FirstLevelCategorySerializer


# SecondLevelCategory


class SecondLevelCategoryListView(generics.ListCreateAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer


class SecondLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SecondLevelCategory.objects.all()
    serializer_class = SecondLevelCategorySerializer


# ThirdLevelCategory


class ThirdLevelCategoryListView(generics.ListCreateAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer


class ThirdLevelCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ThirdLevelCategory.objects.all()
    serializer_class = ThirdLevelCategorySerializer
