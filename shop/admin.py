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


class CollectionColorInline(admin.StackedInline):
    model = collection_models.CollectionColor
    extra = 1


class CollectionInline(admin.StackedInline):
    model = collection_models.Collection
    fields = ('name', 'thumbnail')
    extra = 0


@admin.register(collection_models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionColorInline,]

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


@admin.register(collection_models.CollectionOffer)
class CollectionOfferAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionInline,]
