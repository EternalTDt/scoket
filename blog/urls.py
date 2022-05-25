from django.urls import path
from .views import (
    PostListView,
    PostDetailView,

    CommentListView,
    CommentDetailView,

    TagListView,
    TagDetailView,
)

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListView.as_view(), name='comments'),
    path('comments/<slug:slug>/', CommentDetailView.as_view(), name='comment-detail'),
    path('tags/', TagListView.as_view(), name="tags"),
    path('tags/<slug:slug>/', TagDetailView.as_view(), name="tag-detail"),
]