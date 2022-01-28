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
)

urlpatterns = [
    path('first-level-categories/', FirstLevelCategoryListView.as_view(), name='first-level-categories'),
    path('first-level-categories/<slug:slug>/', FirstLevelCategoryDetailView.as_view(), name='first-level-categories-detail'),
    path('second-level-categories/', SecondLevelCategoryListView.as_view(), name='second-level-categories'),
    path('second-level-categories/<slug:slug>', SecondLevelCategoryDetailView.as_view(), name='second-level-categories-detail'),
    path('third-level-categories/', ThirdLevelCategoryListView.as_view(), name='third-level-categories'),
    path('third-level-categories/<slug:slug>', ThirdLevelCategoryDetailView.as_view(), name='third-level-categories-detail'),
    path('brand/', BrandListView.as_view(), name='brand'),
    path('brand/<slug:slug>', BrandDetailView.as_view(), name='brand-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])