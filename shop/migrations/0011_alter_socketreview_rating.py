# Generated by Django 4.0.4 on 2022-06-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_socketreview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socketreview',
            name='rating',
            field=models.CharField(choices=[(4, 4), (5, 5), (1, 1), (3, 3), (2, 2)], default=5, max_length=2, verbose_name='Рейтинг'),
        ),
    ]