from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order
from django.core.mail import send_mail
from django.conf import settings


@receiver(pre_save, sender=Order)
def on_status_change(sender, instance: Order, **kwargs):
    previous = Order.objects.get(id=instance.id)
    if previous.status !=  instance.status:
        mail_sent = send_mail(
            f'Статус заказа #{instance.order_identificator} изменен',
            f'{instance.user.profile.first_name} {instance.user.profile.patronymic}, \n\n' \
            f'статус вашего заказа изменен на "{instance.status}".',
            settings.EMAIL_HOST_USER,
            [instance.user.email],
            fail_silently=False,
        )
        return mail_sent