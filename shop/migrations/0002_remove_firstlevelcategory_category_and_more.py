# Generated by Django 4.0.1 on 2022-03-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='firstlevelcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='firstlevelcategory',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='second_level_category', to='shop.SecondLevelCategory', verbose_name='Категория'),
        ),
        migrations.RemoveField(
            model_name='secondlevelcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='secondlevelcategory',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='third_level_category', to='shop.ThirdLevelCategory', verbose_name='Категория'),
        ),
    ]
