from django.urls import path
from .views import (OrderListView, OrderDetailView)

urlpatterns = [
    path('create-order/', OrderListView.as_view(), name="order"),
    path('order/<slug:slug>', OrderDetailView.as_view(), name='order-detail'),
]
