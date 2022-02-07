# Generated by Django 4.0.1 on 2022-02-01 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='brand_photos', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренды',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='FirstLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='first_level_cat_photos', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Главная категория',
                'verbose_name_plural': 'Главные категории',
            },
        ),
        migrations.CreateModel(
            name='SecondLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='second_level_cat_photos', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_level_category', to='shop.firstlevelcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория 2 уровня',
                'verbose_name_plural': 'Категории 2 уровня',
            },
        ),
        migrations.CreateModel(
            name='ThirdLevelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('image', models.ImageField(upload_to='third_level_cat_photos', verbose_name='Изображение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_level_category', to='shop.secondlevelcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория 3 уровня',
                'verbose_name_plural': 'Категории 3 уровня',
            },
        ),
        migrations.CreateModel(
            name='CollectionImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='collection_images', verbose_name='Изображение')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='shop.collection')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
