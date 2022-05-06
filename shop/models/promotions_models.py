from django.db import models

class Promotion(models.Model):
    name = models.CharField('Название акции', max_length=60)
    image = models.ImageField("Изоюражение", upload_to='promotions_images')
    promotion_type = models.CharField('Тип акции', max_length=60)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"
