from django.db import models

class WorkingInfo(models.Model):
    working_days = models.CharField("Время работы", max_length=120, help_text="пн. — пт. с 9:00 до 17:30")
    delivery_days = models.CharField("Время доставки", max_length=120, help_text="пн. — пт. с 12:00 до 17:00")
    working_years = models.CharField("Года работы магазина", max_length=20, default='2021')
    shop_address = models.CharField("Адрес магазина", max_length=60, blank=True)

    def __str__(self) -> str:
        return self.working_years

    class Meta:
        verbose_name = "Данные о работе"
        verbose_name_plural = "Данные о работе"


class SocialLinks(models.Model):
    vk_link = models.CharField("Vkontakte", max_length=60, blank=True)
    instagram_link = models.CharField("Instagram", max_length=60, blank=True)
    telegram_link = models.CharField("Telegram", max_length=60, blank=True)
    whatsapp_link = models.CharField("Whatsapp", max_length=60, blank=True)
    viber_link = models.CharField("Viber", max_length=60, blank=True)

    def __str__(self) -> str:
        return 'Ссылка'

    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"



