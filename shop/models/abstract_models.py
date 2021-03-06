from django.db import models
from .brand_models import Brand
from django.contrib.auth.models import User


class AbstractCategory(models.Model):
    name = models.CharField('Название', max_length=60, default='')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    class Meta:
        abstract = True
        app_label="shop"


class AbstractCollection(models.Model):
    name = models.CharField('Название', max_length=60)
    code = models.CharField('Код', max_length=20)
    description = models.TextField('Описание')

    class Meta:
        abstract = True
        app_label="shop"


class AbstractProduct(models.Model):
    name = models.CharField('Название', max_length=60)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)
    code = models.CharField('Код', max_length=20)
    description = models.TextField('Описание')
    manufacturer = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        verbose_name='Производитель',
        blank=True, 
        null=True,
    )
    price = models.DecimalField('Стоимость', decimal_places=2, max_digits=10)
    stock = models.IntegerField('Количество', default=0)
    availability = models.BooleanField('Наличие', default=True)
    favourite = models.ManyToManyField(User, blank=True)


    class Meta:
        abstract = True
        app_label="shop"
