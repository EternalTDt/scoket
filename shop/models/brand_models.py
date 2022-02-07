from django.db import models
from . import abstract_models


class Brand(abstract_models.AbstractCategory):
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='brand_photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    objects = models.Manager()