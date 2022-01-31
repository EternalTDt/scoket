from dataclasses import field
from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import (
     FirstLevelCategory, 
     SecondLevelCategory, 
     ThirdLevelCategory,
     Brand,
)


class BrandAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = Brand
        fields = ('__all__')


@admin.register(FirstLevelCategory)
class FirstLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as = True


@admin.register(SecondLevelCategory)
class SecondLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ThirdLevelCategory)
class ThirdLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    form = BrandAdminForm