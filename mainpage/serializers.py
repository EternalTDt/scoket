from rest_framework import serializers
from .models import OffersSlider, CurrenPromotionsSlider

class OfferSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OffersSlider
        fields = ('__all__')
        lookup_field = 'slug'


class CurrenPromotionsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrenPromotionsSlider
        fields = ('__all__')
        lookup_field = 'slug'
