# Generated by Django 4.0.4 on 2022-05-19 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=60, verbose_name='Город')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('postal_code', models.IntegerField(default=220055, verbose_name='Почтовый индекс')),
            ],
            options={
                'verbose_name': 'Адрес доставки',
                'verbose_name_plural': 'Адреса доставки',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=60, null=True, unique=True, verbose_name='Ссылка')),
                ('first_name', models.CharField(blank=True, max_length=60, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=60, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=60, verbose_name='Отчество')),
                ('phone_number', models.CharField(blank=True, max_length=17, verbose_name='Телефон')),
                ('is_mailing', models.BooleanField(default=False, verbose_name='Подписан на рассылку')),
                ('shipping_addresses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='accounts.shippingaddress', verbose_name='Адрес')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
