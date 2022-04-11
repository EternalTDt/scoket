from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Order
from .serializers import OrderSerializer


# Order

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'slug'
    permission_classes = [AllowAny]