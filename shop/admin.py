from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models
from .models import promotions_models
from .models import reviews_models


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


class ComputerSocketAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.ComputerSocket
        fields = ('__all__')


class DimmerAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Dimmer
        fields = ('__all__')


class ThermostatAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.Thermostat
        fields = ('__all__')


class NetworkFilterAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())

    class Meta:
        model = product_models.NetworkFilter
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
    list_filter = ('category',)
    autocomplete_fields = ['category',]
    prepopulated_fields = {'slug': ('name',)}
    save_as = True


@admin.register(category_models.SecondLevelCategory)
class SecondLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    autocomplete_fields = ['category',]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(category_models.ThirdLevelCategory)
class ThirdLevelCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
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


class SocketColorInline(admin.TabularInline):
    model = product_models.SocketColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class SwitchColorInline(admin.TabularInline):
    model = product_models.SwitchColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class FrameColorInline(admin.TabularInline):
    model = product_models.FrameColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class PlugColorInline(admin.TabularInline):
    model = product_models.PlugColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class ComputerSocketColorInline(admin.TabularInline):
    model = product_models.ComputerSocketColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class DimmerColorInline(admin.TabularInline):
    model = product_models.DimmerColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class ThermostatColorInline(admin.TabularInline):
    model = product_models.ThermostatColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


class NetworkFilterColorInline(admin.TabularInline):
    model = product_models.NetworkFilterColor
    readonly_fields = ('image_preview',)
    extra = 0

    def image_preview(self, obj):
        return obj.image_preview

    image_preview.short_description = 'Предпросмотр изображения'
    image_preview.allow_tags = True


admin.site.register(reviews_models.SocketReview)

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

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(collection_models.CollectionOffer)
class CollectionOfferAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    inlines = [CollectionInline,]


@admin.register(product_models.ProductOffer)
class ProductOfferAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(product_models.Socket)
class SocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'grounding', 'kids_protection', 'backlight',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [SocketColorInline,]
    form = SocketAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('socket_type', 'montage', 'terminal', 'rated_current')
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

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True

    def slugfield(self, obj):
        return 'socket'

@admin.register(product_models.Switch)
class SwitchAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'backlight',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [SwitchColorInline,]
    form = SwitchAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('switch_type', 'montage', 'terminal', 'rated_current')
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

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [FrameColorInline,]
    form = FrameAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('frame_type',)
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

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Plug)
class PlugAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'backlight',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [PlugColorInline,]
    form = PlugAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('plug_type', 'montage', )
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

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.ComputerSocket)
class ComputerSocketAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'grounding', 'kids_protection',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [ComputerSocketColorInline,]
    form = ComputerSocketAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('computer_socket_type', 'montage', )
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': ('socket', 'rated_current', 'grounding', 'protection', 'kids_protection', 'material')
        }),
        ('Размеры', {
            'fields': ('width', 'height', 'depth')
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Dimmer)
class DimmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = ('availability', 'grounding', 'kids_protection', 'backlight',)
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [DimmerColorInline,]
    form = DimmerAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': ('dimmer_type', 'montage', 'terminal')
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': (
                'grounding', 'three_phase_socket', 'control', 'protection', 
                'kids_protection', 'backlight', 'peculiarities', 'material', 'equipment'
                )
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.Thermostat)
class ThermostatAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = (
        'availability',
        'is_smart_home_system_device',
        'air_temperature_sensor',
        'floor_temperature_sensor',
        'wi_fi_control',
        'remote_control',
        'sensor_connection_diagnostics',
        'kids_protection',
        'adaptive_function',
        'manual_mode',
        'calculation_of_consumed_energy',
    )
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [ThermostatColorInline,]
    form = ThermostatAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': (
                'thermostat_type', 'appointment', 'control', 'display', 'is_smart_home_system_device', 'wi_fi_control',
                'air_temperature_sensor','floor_temperature_sensor', 'remote_control', 'montage',
            )
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': (
                'temperature_range', 'temperature_hysteresis', 'remote_sensor_wire_length', 
                'maximum_load_current', 'maximum_load_power', 'correction_of_sensor_readings', 'sensor_connection_diagnostics', 
                'protection_class'
            )
        }),
        ('Программные функции', {
            'fields': (
                'num_of_programs', 
                'num_of_intervals_per_day', 
                'adaptive_function', 
                'manual_mode', 
                'calculation_of_consumed_energy',
                'kids_protection'
            )
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(product_models.NetworkFilter)
class NetworkFilterAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview',)
    list_filter = (
        'availability', 
        'avr', 
        'protective_shutters', 
        'separate_switches', 
        'remote_control',
        'nineteen_rack_mounting',
        'wall_mount',
        'communication_line_protection',
        'overheat_protection',
        'load_short_circuit_protection',
        'over_voltage_protection',
        'remote_control_wi_fi',
    )
    readonly_fields = ('thumbnail_preview', 'type_of')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    save_on_top = True
    save_as = True
    inlines = [NetworkFilterColorInline,]
    form = NetworkFilterAdminForm
    autocomplete_fields = ['category', 'collection']

    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'code', 'description', 'manufacturer', 'thumbnail', 'thumbnail_preview', 'product_offer', 'category', 'collection')
        }),
        ('Основные', {
            'fields': (
                'network_filter_type', 'output_sockets', 'total_number_of_outlets',
                'input_socket', 'avr', 'power_cable', 'protective_shutters', 'separate_switches',
                'remote_control_wi_fi', 'nineteen_rack_mounting', 'wall_mount'
            )
        }),
        ('Информацмонные', {
            'fields': ('price', 'stock', 'availability')
        }),
        ('Технические характеристики', {
            'fields': (
                'rated_current', 'max_input_pulse_energy', 'max_load_current',
                'communication_line_protection', 'indication', 'usb_ports', 
                'overheat_protection', 'load_short_circuit_protection',
                'over_voltage_protection', 'remote_control'
                )
        }),
    )

    def thumbnail_preview(self, obj):
            return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Предпросмотр изображения'
    thumbnail_preview.allow_tags = True


@admin.register(promotions_models.Promotion)
class PromtionAdmin(admin.ModelAdmin):
    list_display = ('name', 'promotion_type',)
    list_filter = ('promotion_type',)
    list_display_links = ('name',)
    search_fields = ('name', 'promotion_type')
    save_as = True
