# Generated by Django 4.0.1 on 2022-02-15 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_thermostat_adaptive_function_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thermostatcolor',
            name='network_filter',
        ),
        migrations.AddField(
            model_name='thermostatcolor',
            name='thermostat',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.thermostat', verbose_name='Терморегулятор'),
        ),
        migrations.AlterField(
            model_name='thermostatcolor',
            name='image',
            field=models.ImageField(upload_to='thermostat_images', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='NetworkFilterColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='networkfilter_images', verbose_name='Изображение')),
                ('network_filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.networkfilter', verbose_name='Сетевой фильтр')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]