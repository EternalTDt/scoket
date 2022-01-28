# Generated by Django 4.0.1 on 2022-01-28 10:43

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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_level_category', to='fakeapi.firstlevelcategory', verbose_name='Категория')),
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
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='third_level_category', to='fakeapi.secondlevelcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория 3 уровня',
                'verbose_name_plural': 'Категории 3 уровня',
            },
        ),
    ]
