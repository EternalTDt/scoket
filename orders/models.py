from django.db import models
from django.contrib.auth.models import User
from shop.models import product_models
from django.utils.crypto import get_random_string
from django.template.defaultfilters import slugify


def generate_order_identificator():
    identifier = get_random_string(6)
    return identifier.upper()


PAYMENT_CHOICES = {
    ('Картой', 'Картой'),
    ('Наличными', 'Наличными'),
}

ORDER_STATUS = {
    ('Создан', 'Создан'),
    ('Принят в обработку', 'Принят в обработку'),
    ('Подтвержден', 'Подтвержден'),
    ('Передан в доставку', 'Передан в доставку'),
    ('Доставлен', 'Доставлен'),
    ('Оплачен', 'Оплачен'),
    ('Отменен', 'Отменен'),
}


class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Клиент", null=True)
    order_identificator = models.CharField("Номер заказа", max_length=6, default=generate_order_identificator)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)
    payment_method = models.CharField("Способ оплаты", max_length=200, choices=PAYMENT_CHOICES, default='Картой')
    status = models.CharField("Статус заказа", max_length=200, choices=ORDER_STATUS, default='Создан')
    created_at = models.DateTimeField('Создано', auto_now_add=True)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    commentary = models.TextField('Комментарий к заказу', max_length=500, blank=True)

    def __str__(self) -> str:
        return f'{self.order_identificator} | {self.created_at}'

    def save(self, *args, **kwargs):
        value = self.order_identificator
        self.slug = slugify(value,)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


# class OrderItem(models.Model):
#     product = models.ForeignKey(product_models.Product, on_delete=models.SET_NULL, null=True)
#     order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     name = models.CharField(max_length=200,null=True,blank=True)
#     qty = models.IntegerField(null=True,blank=True,default=0)
#     price = models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
#     image = models.CharField(max_length=200,null=True,blank=True)
#     _id =  models.AutoField(primary_key=True,editable=False)

#     def __str__(self):
#         return str(self.name)
