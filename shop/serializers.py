from rest_framework import serializers
from .models import category_models
from .models import brand_models
from .models import collection_models

class FirstLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_models.FirstLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = FirstLevelCategorySerializer()

    class Meta:
        model = category_models.SecondLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    category = SecondLevelCategorySerializer()

    class Meta:
        model = category_models.ThirdLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand_models.Brand
        fields = ('__all__')
        lookup_field = 'slug'


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