from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Order
        fields = ('__all__')
        lookup_field = 'slug'
        read_only_fields = ['slug', 'status', 'order_identificator']
