from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models


class BrandAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = brand_models.Brand
        fields = ('__all__')


class SocketAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Socket
        fields = ('__all__')


class SwitchAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Switch
        fields = ('__all__')    


class FrameAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Frame
        fields = ('__all__')


class PlugAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Plug
        fields = ('__all__')


class CollectionAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = collection_models.Collection
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


class SocketColorInline(admin.StackedInline):
    model = product_models.SocketColor
    extra = 1


class SwitchColorInline(admin.StackedInline):
    model = product_models.SwitchColor
    extra = 1


class FrameColorInline(admin.StackedInline):
    model = product_models.FrameColor
    extra = 1


class PlugColorInline(admin.StackedInline):
    model = product_models.PlugColor
    extra = 1


@admin.register(collection_models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionColorInline,]
    form = CollectionAdminForm

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


@admin.register(product_models.Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'grounding', 'kids_protection', 'backlight',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [SocketColorInline,]
    form = SocketAdminForm

    fieldsets = (
        ('Основные', {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'socket_type', 'montage', 'terminal', 'rated_current')
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('socket', 'grounding', 'protection', 'kids_protection', 'backlight', 'material', 'equipment')
        }),
        ('Размеры', {
            'fields': ('width', 'height', 'depth')
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'backlight',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [SwitchColorInline,]
    form = SwitchAdminForm

    fieldsets = (
        ('Основные', {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'switch_type', 'montage', 'terminal', 'rated_current')
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('control', 'frame_places', 'protection', 'backlight', 'material', 'equipment')
        }),
        ('Размеры', {
            'fields': ('width', 'height', 'depth')
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [FrameColorInline,]
    form = FrameAdminForm

    fieldsets = (
        ('Основные', {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'frame_type')
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('frame_places', 'material', 'equipment')
        }),
        ('Размеры', {
            'fields': ('width', 'height', 'depth')
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Plug)
class PlugAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'backlight',)
    readonly_fields = ('thumbnail_preview',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [PlugColorInline,]
    form = PlugAdminForm

    fieldsets = (
        ('Основные', {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'plug_type', 'montage', )
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('protection', 'backlight', 'peculiarities', 'material')
        }),
        ('Размеры', {
            'fields': ('width', 'height', 'depth')
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Изображение'
    thumbnail_preview.allow_tags = True