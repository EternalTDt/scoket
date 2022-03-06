from cgitb import lookup
from rest_framework import serializers
from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models


# Third Level Category

class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category_models.ThirdLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Second Level Category

class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = ThirdLevelCategorySerializer(many=True)

    class Meta:
        model = category_models.SecondLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# First Level Category

class FirstLevelCategorySerializer(serializers.ModelSerializer):
    category = SecondLevelCategorySerializer(many=True)

    class Meta:
        model = category_models.FirstLevelCategory
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


class CollectionOfferSerializer(serializers.ModelSerializer):
    collection = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = collection_models.CollectionOffer
        fields = ('__all__')
        lookup_field = 'slug'


class CollectionSerializer(serializers.ModelSerializer):
    color = CollectionColorSerializer(many=True)
    coolection_offer = CollectionOfferSerializer()

    class Meta:
        model = collection_models.Collection
        fields = ('__all__')
        lookup_field = 'slug'


# Socket

class SocketColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SocketColor
        fields = ('color', 'color_code', 'image')


class SocketSerializer(serializers.ModelSerializer):
    color = CollectionColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

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
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.Switch
        fields = ('__all__')
        lookup_field = 'slug'


# Frame

class FrameColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.FrameColor
        fields = ('color', 'color_code', 'image')


class FrameSerializer(serializers.ModelSerializer):
    color = FrameColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.Frame
        fields = ('__all__')
        lookup_field = 'slug'


# Plug

class PlugColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.PlugColor
        fields = ('color', 'color_code', 'image')


class PlugSerializer(serializers.ModelSerializer):
    color = PlugColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.Plug
        fields = ('__all__')
        lookup_field = 'slug'


# ComputerSocket

class ComputerSocketColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ComputerSocketColor
        fields = ('color', 'color_code', 'image')


class ComputerSocketSerializer(serializers.ModelSerializer):
    color = ComputerSocketColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.ComputerSocket()
        fields = ('__all__')
        lookup_field = 'slug'


# Dimmer

class DimmerColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.DimmerColor
        fields = ('color', 'color_code', 'image')


class DimmerSerializer(serializers.ModelSerializer):
    color = DimmerColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.Dimmer()
        fields = ('__all__')
        lookup_field = 'slug'


# Thermostat

class ThermostatColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ThermostatColor
        fields = ('color', 'color_code', 'image')


class ThermostatSerializer(serializers.ModelSerializer):
    color = ThermostatColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.Thermostat()
        fields = ('__all__')
        lookup_field = 'slug'


# NetworkFilter

class NetworkFilterColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.NetworkFilterColor
        fields = ('color', 'color_code', 'image')


class NetworkFilterSerializer(serializers.ModelSerializer):
    color = NetworkFilterColorSerializer(many=True)
    category = ThirdLevelCategorySerializer()

    class Meta:
        model = product_models.NetworkFilter()
        fields = ('__all__')
        lookup_field = 'slug'
