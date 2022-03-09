# Generated by Django 4.0.1 on 2022-03-09 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_computersocket_depth_computersocket_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='shop.collection', verbose_name='Коллекция'),
        ),
    ]
