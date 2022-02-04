from django.db import models
from . import abstract_models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html

class CollectionOffer(models.Model):
    name = models.CharField('Название', max_length=60)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Предложение"
        verbose_name_plural = "Предложения"


class Collection(abstract_models.AbstractCollection):
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)
    thumbnail = models.ImageField("Изображение", upload_to='collection_images', null=True, blank=True)
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=10)
    manufacturer = models.CharField('Производитель', max_length=60, default='Schneider Electric')
    coolection_offer = models.ForeignKey(CollectionOffer, on_delete=models.CASCADE, verbose_name="Предложение", related_name='collection', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Коллекция"
        verbose_name_plural = "Коллекции"


class CollectionColor(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, verbose_name="Коллекция", related_name='color')
    color = models.CharField('Цвет', max_length=60)
    color_code = models.CharField('Код цвета', max_length=60, default='#fff')
    image = models.ImageField('Изображение', upload_to='collection_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
