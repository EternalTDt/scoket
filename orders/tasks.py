from celery import shared_task 
from django.core.mail import send_mail
from time import sleep
from django.conf import settings
from django.dispatch import receiver
import telegram_send

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Order


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task()
def send_tg_message(order_identificator, first_name, patronymic, payment_method, commentary, phone, city, address, postal_code):
    telegram_send.send(
        messages =
        [f"💸 Заказ #{order_identificator} \n👤 {first_name} {patronymic} \n💳 {payment_method} \n🗣 «{commentary}» \n📞 {phone} \n🏠 {city}, {address}, {postal_code}"]
    )


@shared_task
def send_email(subject, message, host_email, email):
    send_mail(
        subject,
        message,
        host_email,
        [email],
        fail_silently=False,
    )


@shared_task
@receiver(pre_save, sender=Order)
def send_email_on_order_change_status(sender, instance: Order, **kwargs):
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
