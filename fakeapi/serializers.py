from dataclasses import field
from statistics import mode
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token