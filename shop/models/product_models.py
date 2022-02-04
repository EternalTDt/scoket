from django.db import models
from . import abstract_models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html


class Socket(abstract_models.AbstractProduct):
    socket_type = models.CharField("Тип", max_length=20)
    montage = models.CharField("Монтаж", max_length=20)
    terminal = models.CharField("Клемма", max_length=20)
    rated_current = models.CharField("Номинальный ток", max_length=20)
    thumbnail = models.ImageField("Изображение", upload_to='socket_images', null=True, blank=True)

    socket = models.CharField("Розетка", max_length=20)
    grounding = models.BooleanField("Заземление", default=True)
    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    kids_protection = models.BooleanField("Защита от детей", blank=True)
    backlight = models.BooleanField("Подстветка", default=False)
    material = models.CharField("Материал", max_length=20)
    equipment = models.CharField("Комплектация", max_length=60)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

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
        verbose_name = "Розетка"
        verbose_name_plural = "Розетки"


class SocketColor(models.Model):
    socket = models.ForeignKey(
        Socket, 
        on_delete=models.CASCADE, 
        verbose_name="Розетка", 
        related_name='color',
    )
    color = models.CharField('Цвет', max_length=60)
    color_code = models.CharField('Код цвета', max_length=60, default='#fff')
    image = models.ImageField('Изображение', upload_to='socket_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"
