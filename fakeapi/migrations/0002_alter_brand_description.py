# Generated by Django 4.0.1 on 2022-01-31 15:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakeapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]
