from django.db import models


class AbstractCategory(models.Model):
    name = models.CharField('Название', max_length=60, default='')
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    class Meta:
        abstract = True


class AbstractCollection(models.Model):
    name = models.CharField('Название', max_length=60)
    code = models.CharField('Код', max_length=20)
    description = models.TextField('Описание')

    class Meta:
        abstract = True