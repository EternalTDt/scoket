from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer
from .models import Order
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .tasks import send_tg_message, send_email


# Order

class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        order_id = serializer.data['id']
        user_name = serializer.data['user']
        print(order_id, user_name)
        order = Order.objects.get(id=order_id)
        user = User.objects.get(username=user_name)
        email = user.email
        first_name = user.profile.first_name
        patronymic = user.profile.patronymic
        phone = user.profile.phone_number
        city = user.profile.shipping_addresses.city
        address = user.profile.shipping_addresses.address
        postal_code = user.profile.shipping_addresses.postal_code
        order_identificator = order.order_identificator
        payment_method = order.payment_method
        commentary = order.commentary

        host_email = settings.EMAIL_HOST_USER

        subject = f'Заказ #{order_identificator} на сайте protonelectrics.by успешно создан'
        message = f'{first_name} {patronymic}, спасибо за оформление заказа! \n\n' \
            'Более подробную информацию о заказе вы можете найти в своем пофиле в разделе "История заказов" \n\n' \
            'С уважением, команда protonelectrics.by'

        send_tg_message.delay(order_identificator, first_name, patronymic, payment_method, commentary, phone, city, address, postal_code)
        send_email.delay(subject, message, host_email, email)



class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated]