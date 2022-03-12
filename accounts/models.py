from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name='Профиль',
        related_name='profile',
    )
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True, default='')
    first_name = models.CharField("Имя", max_length=60)
    surname = models.CharField("Фамилия", max_length=60)
    patronymic = models.CharField("Отчество", max_length=60)
    phone_number = models.CharField("Телефон", max_length=17)
    city = models.CharField("Город", max_length=60)
    address = models.CharField("Адрес", max_length=120)
    postal_code = models.IntegerField("Почтовый индекс", default=220055)
    is_mailing = models.BooleanField("Подписан на рассылку", default=False)

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
