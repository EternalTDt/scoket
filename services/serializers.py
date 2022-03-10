from rest_framework import serializers
from .models import WorkingInfo, SocialLinks


class WorkingInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkingInfo
        fields = ('__all__')


class SocialLinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialLinks
        fields = ('__all__')
