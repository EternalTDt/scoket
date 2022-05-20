from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    email = serializers.EmailField(source="user.email")
    class Meta:
        model = UserProfile
        fields = ('__all__')
