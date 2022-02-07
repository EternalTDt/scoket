# Generated by Django 4.0.1 on 2022-02-07 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_switch_switch_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('frame_type', models.CharField(max_length=40, verbose_name='Тип')),
                ('frame_places', models.IntegerField(default=1, verbose_name='Количество мест в рамке')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='frame_images', verbose_name='Изображение')),
                ('material', models.CharField(max_length=20, verbose_name='Материал')),
                ('equipment', models.CharField(max_length=60, verbose_name='Комплектация')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
            ],
            options={
                'verbose_name': 'Рамка',
                'verbose_name_plural': 'Рамки',
            },
        ),
        migrations.AddField(
            model_name='socket',
            name='manufacturer',
            field=models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель'),
        ),
        migrations.AddField(
            model_name='switch',
            name='manufacturer',
            field=models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель'),
        ),
        migrations.CreateModel(
            name='FrameColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='frame_images', verbose_name='Изображение')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.frame', verbose_name='Рамка')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]
