from rest_framework import generics
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import WorkingInfo, SocialLinks

from rest_framework import status
from rest_framework.response import Response
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings

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


# Mailchimp


class MailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()



class MailSubscriptionAPIView(generics.GenericAPIView):
    serializer_class = MailSerializer

    def subscribe_email(email, first_name, last_name, phone):
        '''
        This func will communicate with Mailchimp api
        to create a member in audience list
        '''
        mailchimp = Client()
        mailchimp.set_config({
            'api_key': settings.MAILCHIMP_API_KEY,
            'server': settings.MAILCHIMP_DATACENTER,
        })
        member_info = {
            'email_address': email,
            'status': 'subscribed',
            'merge_fields': {
                'FNAME': first_name,
                'LNAME': last_name,
                'PHONE': phone,
            },
        }

        try:
            mailchimp.lists.add_list_member(settings.MAILCHIMP_LIST_ID, member_info)
        except ApiClientError as error:
            print(error.text)

    def post(self, request, *args, **kwargs):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        phone = request.data['phone']
        MailSubscriptionAPIView.subscribe_email(email, first_name, last_name, phone)
        return Response({
            'status_code': status.HTTP_200_OK,
            'message': 'Mail successfully added to audience list',
        })
