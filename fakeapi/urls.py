from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    FirstLevelCategoryListView, 
    FirstLevelCategoryDetailView,

    SecondLevelCategoryListView, 
    SecondLevelCategoryDetailView,

    ThirdLevelCategoryListView,
    ThirdLevelCategoryDetailView,
)

urlpatterns = [
    path('first-level-categories/', FirstLevelCategoryListView.as_view()),
    path('first-level-categories/<int:pk>/', FirstLevelCategoryDetailView.as_view()),
    path('second-level-categories/', SecondLevelCategoryListView.as_view()),
    path('second-level-categories/<int:pk>', SecondLevelCategoryDetailView.as_view()),
    path('third-level-categories/', ThirdLevelCategoryListView.as_view()),
    path('third-level-categories/<int:pk>', ThirdLevelCategoryDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])