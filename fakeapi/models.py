from django.db import models
from django.urls import reverse


class AbstractCategory(models.Model):
    name = models.CharField('Название', max_length=60, default='')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    class Meta:
        abstract = True


class FirstLevelCategory(AbstractCategory):
    image = models.ImageField('Изображение', upload_to='first_level_cat_photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"

    objects = models.Manager()


class SecondLevelCategory(AbstractCategory):
    category = models.ForeignKey(FirstLevelCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='second_level_category')
    image = models.ImageField('Изображение', upload_to='second_level_cat_photos')

    def __str__(self) -> str:
        return f'{self.category.name}: {self.name}'

    class Meta:
        verbose_name = "Категория 2 уровня"
        verbose_name_plural = "Категории 2 уровня"

    objects = models.Manager()


class ThirdLevelCategory(AbstractCategory):
    category = models.ForeignKey(SecondLevelCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='third_level_category')
    image = models.ImageField('Изображение', upload_to='third_level_cat_photos')

    def __str__(self) -> str:
        return f'{self.category.name}: {self.name}'

    class Meta:
        verbose_name = "Категория 3 уровня"
        verbose_name_plural = "Категории 3 уровня"

    objects = models.Manager()


class Brand(AbstractCategory):
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='brand_photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    objects = models.Manager()