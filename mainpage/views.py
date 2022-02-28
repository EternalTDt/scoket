from cgitb import lookup
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import OffersSlider, CurrenPromotionsSlider
from .serializers import OfferSliderSerializer, CurrenPromotionsSliderSerializer


# Offers slider

class OffersSliderListView(generics.ListAPIView):
    queryset = OffersSlider.objects.all()
    serializer_class = OfferSliderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class OffersSliderDetailView(generics.RetrieveAPIView):
    queryset = OffersSlider.objects.all()
    serializer_class = OfferSliderSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]


# Current promotions slider

class CurrenPromotionsSliderListView(generics.ListAPIView):
    queryset = CurrenPromotionsSlider.objects.all()
    serializer_class = CurrenPromotionsSliderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class CurrenPromotionsSliderDetailView(generics.RetrieveAPIView):
    queryset = CurrenPromotionsSlider.objects.all()
    serializer_class = CurrenPromotionsSliderSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
