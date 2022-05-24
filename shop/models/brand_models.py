from django.db import models


class Brand(models.Model):
    name = models.CharField('Название', max_length=60, default='')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='brand_photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    objects = models.Manager()