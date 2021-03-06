# Generated by Django 4.0.4 on 2022-05-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Наличными', 'Наличными'), ('Картой', 'Картой')], default='Картой', max_length=200, verbose_name='Способ оплаты'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Передан в доставку', 'Передан в доставку'), ('Доставлен', 'Доставлен'), ('Отменен', 'Отменен'), ('Подтвержден', 'Подтвержден'), ('Оплачен', 'Оплачен'), ('Создан', 'Создан'), ('Принят в обработку', 'Принят в обработку')], default='Создан', max_length=200, verbose_name='Статус заказа'),
        ),
    ]
