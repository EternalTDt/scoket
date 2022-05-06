from celery import shared_task 
from django.core.mail import send_mail
from time import sleep
from django.conf import settings
from requests import request
import telegram_send

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

@shared_task()
def send_email(subject, message, host_email, email):
    send_mail(
        subject,
        message,
        host_email,
        [email],
        fail_silently=False,
    )