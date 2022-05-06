from django.db import models
from . import abstract_models


class ThirdLevelCategory(abstract_models.AbstractCategory):
    image = models.ImageField('Изображение', upload_to='third_level_cat_photos')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория 3 уровня"
        verbose_name_plural = "Категории 3 уровня"

    objects = models.Manager()


class SecondLevelCategory(abstract_models.AbstractCategory):
    category = models.ManyToManyField(
        ThirdLevelCategory,
        verbose_name='Категория',
        related_name='third_level_category',
        blank=True,
    )
    image = models.ImageField('Изображение', upload_to='second_level_cat_photos')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория 2 уровня"
        verbose_name_plural = "Категории 2 уровня"

    objects = models.Manager()



class FirstLevelCategory(abstract_models.AbstractCategory):
    category = models.ManyToManyField(
        SecondLevelCategory,
        verbose_name='Категория',
        related_name='second_level_category',
        blank=True,
    )
    image = models.ImageField('Изображение', upload_to='first_level_cat_photos')

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "Категория 1 уровня"
        verbose_name_plural = "Категории 1 уровня"

    objects = models.Manager()
