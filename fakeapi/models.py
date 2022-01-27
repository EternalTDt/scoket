from django.db import models

class FirstLevelCategory(models.Model):
    name = models.CharField('Название', max_length=60)
    image = models.ImageField('Изображение', upload_to='first_level_cat_photos')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Главная категория"
        verbose_name_plural = "Главные категории"


class SecondLevelCategory(models.Model):
    name = models.CharField('Название', max_length=60)
    category = models.ForeignKey(FirstLevelCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategory')
    image = models.ImageField('Изображение', upload_to='second_level_cat_photos')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self) -> str:
        return f'{self.category.name}: {self.name}'

    class Meta:
        verbose_name = "Категория 2 уровня"
        verbose_name_plural = "Категории 2 уровня"


class ThirdLevelCategory(models.Model):
    name = models.CharField('Название', max_length=60)
    category = models.ForeignKey(SecondLevelCategory, on_delete=models.CASCADE, verbose_name='Категория', related_name='subcategory')
    image = models.ImageField('Изображение', upload_to='third_level_cat_photos')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self) -> str:
        return f'{self.category.name}: {self.name}'

    class Meta:
        verbose_name = "Категория 3 уровня"
        verbose_name_plural = "Категории 3 уровня"
