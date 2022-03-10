from django_filters import rest_framework as filters
from .models import product_models


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SocketFilter(filters.FilterSet):
    price = filters.RangeFilter()

    class Meta:
        model = product_models.Socket
        fields = [
            'price', 
            'availability', 
            'manufacturer', 
            'socket_type', 
            'montage', 
            'terminal', 
            'rated_current',
            'grounding',
            'protection',
            'kids_protection',
            'backlight',
            'material',
        ]