# Generated by Django 4.0.4 on 2022-05-24 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_collection_collectioncolor_collection_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='computersocket',
            name='type_of',
            field=models.CharField(default='computer-socket', max_length=60),
        ),
        migrations.AddField(
            model_name='dimmer',
            name='type_of',
            field=models.CharField(default='dimmer', max_length=60),
        ),
        migrations.AddField(
            model_name='frame',
            name='type_of',
            field=models.CharField(default='frame', max_length=60),
        ),
        migrations.AddField(
            model_name='networkfilter',
            name='type_of',
            field=models.CharField(default='network-filter', max_length=60),
        ),
        migrations.AddField(
            model_name='plug',
            name='type_of',
            field=models.CharField(default='plug', max_length=60),
        ),
        migrations.AddField(
            model_name='socket',
            name='type_of',
            field=models.CharField(default='socket', max_length=60),
        ),
        migrations.AddField(
            model_name='switch',
            name='type_of',
            field=models.CharField(default='switch', max_length=60),
        ),
        migrations.AddField(
            model_name='thermostat',
            name='type_of',
            field=models.CharField(default='thermostat', max_length=60),
        ),
    ]
