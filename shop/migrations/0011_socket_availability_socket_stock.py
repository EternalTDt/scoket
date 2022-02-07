# Generated by Django 4.0.1 on 2022-02-04 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_remove_socket_socket_offer_delete_productoffer'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='availability',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='socket',
            name='stock',
            field=models.IntegerField(default=0, verbose_name='Количество'),
        ),
    ]
