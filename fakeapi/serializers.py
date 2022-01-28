from rest_framework import serializers
from .models import ( 
    FirstLevelCategory, 
    SecondLevelCategory, 
    ThirdLevelCategory,
    Brand,
)


class FirstLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = FirstLevelCategorySerializer()

    class Meta:
        model = SecondLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    category = SecondLevelCategorySerializer()

    class Meta:
        model = ThirdLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')
        lookup_field = 'slug'
