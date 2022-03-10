from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import WorkingInfo, SocialLinks

from .serializers import (
    WorkingInfoSerializer,
    SocialLinksSerializer
)


#  Working Info

class WorkingInfoListView(generics.ListAPIView):
    queryset = WorkingInfo.objects.all()
    serializer_class = WorkingInfoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Social Links

class SocialLinksListView(generics.ListAPIView):
    queryset = SocialLinks.objects.all()
    serializer_class = SocialLinksSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
