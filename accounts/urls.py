from django.urls import path

from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    # get all user profiles and create a new profile
    path("profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
   # retrieve profile details of the currently logged in user
    path("profiles/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
]
