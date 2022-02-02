from tabnanny import verbose
from django.db import models
from . import abstract_models


class AbstractCollection(models.Model):
    name = models.CharField('Название', max_length=60)
    code = models.CharField('Код', max_length=20)
    description = models.TextField('Описание')
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=10)

    class Meta:
        abstract = True


class Collection(AbstractCollection):
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class CollectionColor(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField('Цвет', max_length=60)
    color_code = models.CharField('Код цвета', max_length=60, default='#fff')
    image = models.ImageField('Изображение', upload_to='collection_images')

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"