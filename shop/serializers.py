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
        fields = ('color', 'image')


class CollectionOfferSerializer(serializers.ModelSerializer):
    collection = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = collection_models.CollectionOffer
        fields = ('__all__')
        lookup_field = 'slug'


class CollectionSerializer(serializers.ModelSerializer):
    coolection_offer = CollectionOfferSerializer()
    color = CollectionColorSerializer(many=True)
    sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    switches = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    plugs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    frames = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    computer_sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    dimmers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    thermostats = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    network_filters = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')


    class Meta:
        model = collection_models.Collection
        fields = ('__all__')
        lookup_field = 'slug'


class ProductOfferSerializer(serializers.ModelSerializer):                                                            

    class Meta:
        model = product_models.ProductOffer
        fields = ('__all__')
        lookup_field = 'slug'


# Socket

class SocketColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SocketColor
        fields = ('color', 'image')


class SocketSerializer(serializers.ModelSerializer):
    color = SocketColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Socket
        fields = ('__all__')
        lookup_field = 'slug'


# Switch

class SwitchColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SwitchColor
        fields = ('color', 'image')


class SwitchSerializer(serializers.ModelSerializer):
    color = SwitchColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Switch
        fields = ('__all__')
        lookup_field = 'slug'


# Frame

class FrameColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.FrameColor
        fields = ('color', 'image')


class FrameSerializer(serializers.ModelSerializer):
    color = FrameColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Frame
        fields = ('__all__')
        lookup_field = 'slug'


# Plug

class PlugColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.PlugColor
        fields = ('color', 'image')


class PlugSerializer(serializers.ModelSerializer):
    color = PlugColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Plug
        fields = ('__all__')
        lookup_field = 'slug'


# ComputerSocket

class ComputerSocketColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ComputerSocketColor
        fields = ('color', 'image')


class ComputerSocketSerializer(serializers.ModelSerializer):
    color = ComputerSocketColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.ComputerSocket()
        fields = ('__all__')
        lookup_field = 'slug'


# Dimmer

class DimmerColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.DimmerColor
        fields = ('color', 'image')


class DimmerSerializer(serializers.ModelSerializer):
    color = DimmerColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Dimmer()
        fields = ('__all__')
        lookup_field = 'slug'


# Thermostat

class ThermostatColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ThermostatColor
        fields = ('color', 'image')


class ThermostatSerializer(serializers.ModelSerializer):
    color = ThermostatColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.Thermostat()
        fields = ('__all__')
        lookup_field = 'slug'


# NetworkFilter

class NetworkFilterColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.NetworkFilterColor
        fields = ('color', 'image')


class NetworkFilterSerializer(serializers.ModelSerializer):
    color = NetworkFilterColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = CollectionSerializer()
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    class Meta:
        model = product_models.NetworkFilter()
        fields = ('__all__')
        lookup_field = 'slug'
