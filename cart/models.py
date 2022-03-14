from tabnanny import verbose
from django.db import models
from shop.models import product_models
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    products = models.ForeignKey(
        product_models.Products,
        on_delete=models.SET_NULL,
        verbose_name="Товары",
        blank=True,
        null=True,
    )
    quantity = models.IntegerField("Количество", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self) -> str:
        return f'{self.user.profile.first_name} {self.user.profile.surname}'

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"



