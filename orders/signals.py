from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from django.conf import settings


@receiver(pre_save, sender=Order)
def on_change(sender, instance: Order, **kwargs):
    if instance.id is None: # new object will be created
        pass # write your code here
    else:
        previous = sender.objects.get(id=instance.id)
        if previous.status != instance.status: # field will be updated
            send_mail(
                f'Статус заказа #{previous.order_identificator} изменен',
                f'{previous.user.profile.first_name} {previous.user.profile.patronymic}, \n\n' \
                f'Cтатус вашего заказа изменен на "{instance.status}".',
                settings.EMAIL_HOST_USER,
                [previous.user.email],
                fail_silently=False,
            )