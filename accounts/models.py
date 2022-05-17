from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class ShippingAddress(models.Model):
    city = models.CharField("Город", max_length=60)
    address = models.CharField("Адрес", max_length=120)
    postal_code = models.IntegerField("Почтовый индекс", default=220055)

    def __str__(self):
        return f'{self.city}, {self.address}, {self.postal_code}'

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Профиль',
        related_name='profile',
    )
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=60, blank=True)
    surname = models.CharField("Фамилия", max_length=60, blank=True)
    patronymic = models.CharField("Отчество", max_length=60, blank=True)
    phone_number = models.CharField("Телефон", max_length=17, blank=True)
    is_mailing = models.BooleanField("Подписан на рассылку", default=False)
    shipping_addresses = models.ForeignKey(
        ShippingAddress, 
        on_delete=models.CASCADE, 
        related_name="user", 
        verbose_name="Адрес", 
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
