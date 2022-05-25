from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Профиль',
        related_name='profile',
    )
    first_name = models.CharField("Имя", max_length=60, blank=True)
    surname = models.CharField("Фамилия", max_length=60, blank=True)
    patronymic = models.CharField("Отчество", max_length=60, blank=True)
    phone_number = models.CharField("Телефон", max_length=17, blank=True)
    is_mailing = models.BooleanField("Подписан на рассылку", default=False)
    address = models.CharField("Адрес", max_length=155, blank=True)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
