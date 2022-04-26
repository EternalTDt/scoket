from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .models import Order
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


# Order

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        order_id = serializer.data['id']
        user_name = serializer.data['user']
        order = Order.objects.get(id=order_id)
        user = User.objects.get(username=user_name)

        host_email = settings.EMAIL_HOST_USER

        subject = f'Заказ #{order.order_identificator} на сайте protonelectrics.by успешно создан'
        message = f'{user.profile.first_name} {user.profile.patronymic}, спасибо за оформление заказа! \n\n' \
            'Более подробную информацию о заказе вы можете найти в своем пофиле в разделе "История заказов" \n\n' \
            'С уважением, команда protonelectrics.by'
        
        mail_sent = send_mail(
            subject,
            message,
            host_email,
            [user.email],
            fail_silently=False,
        )
        return mail_sent


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]