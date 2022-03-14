# Generated by Django 4.0.1 on 2022-03-11 13:11

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60, verbose_name='Имя')),
                ('surname', models.CharField(max_length=60, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=60, verbose_name='Отчество')),
                ('phone_number', models.CharField(max_length=17, verbose_name='Телефон')),
                ('city', models.CharField(max_length=60, verbose_name='Город')),
                ('address', models.CharField(max_length=120, verbose_name='Адрес')),
                ('postal_code', models.IntegerField(default=220055, verbose_name='Почтовый индекс')),
                ('is_mailing', models.BooleanField(default=False, verbose_name='Подписан на рассылку')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Профиль')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
