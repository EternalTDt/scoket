from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import category_models
from .models import brand_models
from .models import collection_models


class BrandAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = brand_models.Brand
        fields = ('__all__')


@admin.register(category_models.FirstLevelCategory)
class FirstLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_as = True


@admin.register(category_models.SecondLevelCategory)
class SecondLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(category_models.ThirdLevelCategory)
class ThirdLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(brand_models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    form = BrandAdminForm


class CollectionImageInline(admin.TabularInline):
    model = collection_models.CollectionImage
    extra = 3


@admin.register(collection_models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionImageInline,]