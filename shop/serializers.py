from cgitb import lookup
from rest_framework import serializers
from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models


# First Level Category

class FirstLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_models.FirstLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Second Level Category

class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = FirstLevelCategorySerializer()

    class Meta:
        model = category_models.SecondLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Third Level Category

class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    category = SecondLevelCategorySerializer()

    class Meta:
        model = category_models.ThirdLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand_models.Brand
        fields = ('__all__')
        lookup_field = 'slug'


# Collection

class CollectionColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = collection_models.CollectionColor
        fields = ('color', 'color_code', 'image')


class CollectionSerializer(serializers.ModelSerializer):
    color = CollectionColorSerializer(many=True)

    class Meta:
        model = collection_models.Collection
        fields = ('__all__')
        lookup_field = 'slug'


class CollectionOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = collection_models.CollectionOffer
        fields = ('__all__')
        lookup_field = 'slug'


# Socket

class SocketColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SocketColor
        fields = ('color', 'color_code', 'image')


class SocketSerializer(serializers.ModelSerializer):
    color = CollectionColorSerializer(many=True)

    class Meta:
        model = product_models.Socket
        fields = ('__all__')
        lookup_field = 'slug'


# Switch

class SwitchColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SwitchColor
        fields = ('color', 'color_code', 'image')


class SwitchSerializer(serializers.ModelSerializer):
    color = SwitchColorSerializer(many=True)

    class Meta:
        model = product_models.Switch
        fields = ('__all__')
        lookup_field = 'slug'