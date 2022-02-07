from tabnanny import verbose
from django.db import models


class AbstractSliderOffer(models.Model):
    name = models.CharField("Название", max_length=60)
    image = models.ImageField("Изображение", upload_to="slider_images")
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    class Meta:
        abstract = True


class OffersSlider(AbstractSliderOffer):
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Слайдер предложений"
        verbose_name_plural = "Слайдеры предложений"


class CurrenPromotionsSlider(AbstractSliderOffer):

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Слайдер акций"
        verbose_name_plural = "Слайдеры акций"
