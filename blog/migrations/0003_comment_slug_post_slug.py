# Generated by Django 4.0.1 on 2022-03-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default='', max_length=60, unique=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', max_length=60, unique=True, verbose_name='Ссылка'),
        ),
    ]