from dataclasses import field
from rest_framework import serializers
from .models import FirstLevelCategory, SecondLevelCategory, ThirdLevelCategory


class FirstLevelCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstLevelCategory
        fields = ('__all__')


class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = FirstLevelCategorySerializer()

    class Meta:
        model = SecondLevelCategory
        fields = ('__all__')


class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    category = SecondLevelCategorySerializer()

    class Meta:
        model = ThirdLevelCategory
        fields = ('__all__')
