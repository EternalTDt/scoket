from django.contrib import admin
from .models import OffersSlider, CurrenPromotionsSlider


@admin.register(OffersSlider)
class OffersSliderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as = True


@admin.register(CurrenPromotionsSlider)
class CurrenPromotionsSliderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as = True