# Generated by Django 4.0.1 on 2022-02-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_socket_availability_socket_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('switch_type', models.CharField(max_length=20, verbose_name='Тип')),
                ('montage', models.CharField(max_length=20, verbose_name='Монтаж')),
                ('terminal', models.CharField(max_length=20, verbose_name='Клемма')),
                ('rated_current', models.CharField(max_length=20, verbose_name='Номинальный ток')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='switch_images', verbose_name='Изображение')),
                ('control', models.CharField(max_length=60, verbose_name='Управление')),
                ('frame_places', models.IntegerField(default=1, verbose_name='Количество мест в рамке')),
                ('protection', models.CharField(max_length=20, verbose_name='Пылевлагозащищенность')),
                ('backlight', models.BooleanField(default=False, verbose_name='Подсветка')),
                ('material', models.CharField(max_length=20, verbose_name='Материал')),
                ('equipment', models.CharField(max_length=60, verbose_name='Комплектация')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
            ],
            options={
                'verbose_name': 'Переключатель',
                'verbose_name_plural': 'Переключатели',
            },
        ),
        migrations.AlterField(
            model_name='socket',
            name='backlight',
            field=models.BooleanField(default=False, verbose_name='Подсветка'),
        ),
        migrations.CreateModel(
            name='SwitchColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='switch_images', verbose_name='Изображение')),
                ('switch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.switch', verbose_name='Переключатель')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]
