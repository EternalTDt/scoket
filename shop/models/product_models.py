from django.db import models
from . import abstract_models
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
from .category_models import ThirdLevelCategory
from .collection_models import Collection
from colorfield.fields import ColorField

class ProductOffer(models.Model):
    name = models.CharField('Название', max_length=60)
    slug = models.SlugField("Ссылка", max_length=60, db_index=True, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Предложение для товаров"
        verbose_name_plural = "Предложения для товаров"

# Socket

class Socket(abstract_models.AbstractProduct):
    socket_type = models.CharField("Тип", max_length=20)
    montage = models.CharField("Монтаж", max_length=20)
    terminal = models.CharField("Клемма", max_length=20)
    rated_current = models.IntegerField("Номинальный ток, А", default=0)
    thumbnail = models.ImageField("Изображение", upload_to='socket_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='sockets', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='sockets',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="sockets",
        blank=True,
        null=True,
    )

    socket = models.CharField("Розетка", max_length=20)
    grounding = models.BooleanField("Заземление", default=True)
    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    kids_protection = models.BooleanField("Защита от детей", blank=True)
    backlight = models.BooleanField("Подсветка", default=False)
    material = models.CharField("Материал", max_length=20)
    equipment = models.CharField("Комплектация", max_length=60)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='socket')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Розетка"
        verbose_name_plural = "1. Розетки"


class SocketColor(models.Model):
    socket = models.ForeignKey(
        Socket, 
        on_delete=models.CASCADE, 
        verbose_name="Розетка", 
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='socket_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# Switch

class Switch(abstract_models.AbstractProduct):
    switch_type = models.CharField("Тип", max_length=40)
    montage = models.CharField("Монтаж", max_length=20)
    terminal = models.CharField("Клемма", max_length=20)
    rated_current = models.IntegerField("Номинальный ток, А", default=0)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='switches', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='switches',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="switches",
        blank=True,
        null=True,
    )
    
    thumbnail = models.ImageField("Изображение", upload_to='switch_images', null=True, blank=True)
    control = models.CharField("Управление", max_length=60)
    frame_places = models.IntegerField("Количество мест в рамке", default=1)
    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    backlight = models.BooleanField("Подсветка", default=False)
    material = models.CharField("Материал", max_length=20)
    equipment = models.CharField("Комплектация", max_length=60)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='switch')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Переключатель"
        verbose_name_plural = "2. Переключатели"
        app_label="shop"


class SwitchColor(models.Model):
    switch = models.ForeignKey(
        Switch, 
        on_delete=models.CASCADE, 
        verbose_name="Переключатель", 
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='switch_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# Frame

class Frame(abstract_models.AbstractProduct):
    frame_type = models.CharField("Тип", max_length=40)
    frame_places = models.IntegerField("Количество мест в рамке", default=1)
    thumbnail = models.ImageField("Изображение", upload_to='frame_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='frames', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='frames',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="frames",
        blank=True,
        null=True,
    )

    material = models.CharField("Материал", max_length=20)
    equipment = models.CharField("Комплектация", max_length=60)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='frame')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Рамка"
        verbose_name_plural = "3. Рамки"
        app_label="shop"


class FrameColor(models.Model):
    frame = models.ForeignKey(
        Frame,
        on_delete=models.CASCADE,
        verbose_name="Рамка",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='frame_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# Plug

class Plug(abstract_models.AbstractProduct):
    plug_type = models.CharField("Тип", max_length=40)
    montage = models.CharField("Монтаж", max_length=20)
    thumbnail = models.ImageField("Изображение", upload_to='plug_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='plugs', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='plugs',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="plugs",
        blank=True,
        null=True,
    )

    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    backlight = models.BooleanField("Подсветка", default=False)
    peculiarities = models.CharField("Особенности", max_length=60)
    material = models.CharField("Материал", max_length=20)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='plug')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Заглушка"
        verbose_name_plural = "4. Заглушки"
        app_label="shop"


class PlugColor(models.Model):
    plug = models.ForeignKey(
        Plug,
        on_delete=models.CASCADE,
        verbose_name="Заглушка",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='plug_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# ComputerSocket

class ComputerSocket(abstract_models.AbstractProduct):
    computer_socket_type = models.CharField("Тип", max_length=40)
    montage = models.CharField("Монтаж", max_length=20)
    thumbnail = models.ImageField("Изображение", upload_to='computer_socket_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='computer_sockets', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='computer_sockets',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="computer_sockets",
        blank=True,
        null=True,
    )

    rated_current = models.IntegerField("Номинальный ток, А", default=0)
    socket = models.CharField("Розетка", max_length=20)
    grounding = models.BooleanField("Заземление", default=True)
    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    kids_protection = models.BooleanField("Защита от детей", blank=True)
    material = models.CharField("Материал", max_length=20)
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='computer-socket')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Компьютерная розетка"
        verbose_name_plural = "5. Компьютерные розетки"
        app_label="shop"


class ComputerSocketColor(models.Model):
    computer_socket = models.ForeignKey(
        ComputerSocket,
        on_delete=models.CASCADE,
        verbose_name="Компьютерная розетка",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='computer_socket_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# Dimmer

class Dimmer(abstract_models.AbstractProduct):
    dimmer_type = models.CharField("Тип", max_length=20)
    montage = models.CharField("Монтаж", max_length=20)
    thumbnail = models.ImageField("Изображение", upload_to='dimmer_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='dimmers', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='dimmers',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="dimmers",
        blank=True,
        null=True,
    )

    terminal = models.CharField("Клемма", max_length=20)
    grounding = models.BooleanField("Заземление", default=True)
    three_phase_socket = models.BooleanField("Трехфазная розетка", default=False)
    control = models.CharField("Управление", max_length=60)
    protection = models.CharField("Пылевлагозащищенность", max_length=20)
    kids_protection = models.BooleanField("Защита от детей", blank=True)
    backlight = models.BooleanField("Подсветка", default=False)
    peculiarities = models.CharField("Особенности", max_length=60)
    material = models.CharField("Материал", max_length=20)
    equipment = models.CharField("Комплектация", max_length=60)    
    width = models.IntegerField("Ширина", default=0)
    height = models.IntegerField("Высота", default=0)
    depth = models.IntegerField("Глубина", default=0)
    type_of = models.CharField(max_length=60, default='dimmer')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Диммер"
        verbose_name_plural = "6. Диммеры"
        app_label="shop"


class DimmerColor(models.Model):
    dimmer = models.ForeignKey(
        Dimmer,
        on_delete=models.CASCADE,
        verbose_name="Диммер",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='dimmer_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# Thermostat

class Thermostat(abstract_models.AbstractProduct):
    from django.core.validators import MaxValueValidator, MinValueValidator
    
    thermostat_type = models.CharField("Тип", max_length=30)
    is_smart_home_system_device = models.BooleanField("Устройство системы 'Умный дом'", default=False)
    appointment = models.CharField("Назначение", max_length=60)
    control = models.CharField("Управление", max_length=60)
    display = models.CharField("Экран", max_length=60)
    air_temperature_sensor = models.BooleanField("Датчик температуры воздуха", blank=True)
    floor_temperature_sensor = models.BooleanField("Датчик температуры пола", blank=True)
    wi_fi_control = models.BooleanField("Управление через Wi-Fi", default=False, blank=True)
    remote_control = models.BooleanField("Пульт ДУ", blank=True)
    montage = models.CharField("Монтаж", max_length=20)
    thumbnail = models.ImageField("Изображение", upload_to='thermostat_images', null=True, blank=True)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='thermostats', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='thermostats',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="thermostats",
        blank=True,
        null=True,
    )

    temperature_range = models.IntegerField(
        "Диапазон температур, °C", 
        default=1, 
        validators = [MaxValueValidator(100), MinValueValidator(1)]
    )
    remote_sensor_wire_length = models.IntegerField("Длина провода выносного датчика, м.", default=3, blank=True)
    temperature_hysteresis = models.FloatField("Температурный гистерезис, °C", default=0, blank=True)
    maximum_load_current = models.IntegerField("Максимальный ток нагрузки, А", default=16, blank=True)
    maximum_load_power = models.IntegerField("Максимальная мощность нагрузки, Вт", default=3000, blank=True)
    correction_of_sensor_readings = models.IntegerField("Коррекция показаний датчика, °C", default=10, blank=True)
    sensor_connection_diagnostics = models.BooleanField("Диагностика подключения датчика", default=True, blank=True)
    protection_class = models.CharField("Класс защиты корпуса", max_length=20, default="IP20")
    kids_protection = models.BooleanField("Защита от детей", default=False)
    num_of_programs = models.IntegerField("Количество программ", default=0, blank=True)
    num_of_intervals_per_day = models.IntegerField("Количество интервалов в сутки", default=2, blank=True)
    adaptive_function = models.BooleanField("Адаптивная функция", default=True, blank=True)
    manual_mode = models.BooleanField("Ручной режим", default=True)
    calculation_of_consumed_energy = models.BooleanField("Расчет потребленной энергии", default=True, blank=True)
    type_of = models.CharField(max_length=60, default='thermostat')


    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Терморегулятор"
        verbose_name_plural = "7. Терморегуляторы"
        app_label="shop"


class ThermostatColor(models.Model):
    thermostat = models.ForeignKey(
        Thermostat,
        on_delete=models.CASCADE,
        verbose_name="Терморегулятор",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='thermostat_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


# NetworkFilter

class NetworkFilter(abstract_models.AbstractProduct):
    network_filter_type = models.CharField("Тип", max_length=30)
    output_sockets = models.CharField("Выходные розетки", max_length=30)
    total_number_of_outlets = models.IntegerField("Общее количество выходных розеток", default=4)
    input_socket = models.CharField("Входная розетка", max_length=30)
    product_offer = models.ForeignKey(
        ProductOffer, 
        on_delete=models.CASCADE, 
        verbose_name="Предложение", 
        related_name='network_filters', 
        blank=True, 
        null=True
    )
    category = models.ForeignKey(
        ThirdLevelCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name='network_filters',
        blank=True,
        null=True,
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        verbose_name="Коллекция",
        related_name="network_filters",
        blank=True,
        null=True,
    )

    avr = models.BooleanField("Автоматическая стабилизация напряжения", default=False)
    power_cable = models.IntegerField("Кабель питания, м.", default=5)
    protective_shutters = models.BooleanField("Защитные шторки/крышки на розетках", default=False)
    separate_switches = models.BooleanField("Раздельные выключатели", default=False)
    remote_control_wi_fi = models.BooleanField("Удаленное управление (Wi-Fi)", default=False)
    nineteen_rack_mounting = models.BooleanField("Монтаж в 19' стойку", default=False)
    wall_mount = models.BooleanField("Крепление к стене", default=False)
    rated_current = models.IntegerField("Номинальное входное напряжение, В", default=220)
    max_input_pulse_energy = models.IntegerField("Макс. энергия входного импульса, Дж", default=125)
    max_load_current = models.IntegerField("Макс. ток нагрузки, А", default=10)
    communication_line_protection = models.BooleanField("Защита линий связи", default=False)
    indication = models.CharField("Индикация", max_length=60)
    usb_ports = models.IntegerField("Usb-порты", default=0)
    overheat_protection = models.BooleanField("Защита от перегрева", default=False)
    load_short_circuit_protection = models.BooleanField("Защита от КЗ", default=False)
    over_voltage_protection = models.BooleanField("Защита от повышения напряжения", default=False)
    remote_control = models.BooleanField("Пульт ДУ", blank=True)
    thumbnail = models.ImageField("Изображение", upload_to='networkfilter_images', null=True, blank=True)
    type_of = models.CharField(max_length=60, default='network-filter')

    def __str__(self) -> str:
        return f'{self.code}: {self.name}'

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            _thumbnail = get_thumbnail(self.thumbnail,
                                      '250x120',
                                      upscale=False,
                                      crop=False,
                                      quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_thumbnail.url, _thumbnail.width, _thumbnail.height))
        return ""

    class Meta:
        verbose_name = "Сетевой фильтр"
        verbose_name_plural = "8. Сетевые фильтры"
        app_label="shop"


class NetworkFilterColor(models.Model):
    network_filter = models.ForeignKey(
        NetworkFilter,
        on_delete=models.CASCADE,
        verbose_name="Сетевой фильтр",
        related_name='color',
    )
    color = ColorField('Цвет', image_field='image')
    image = models.ImageField('Изображение', upload_to='networkfilter_images')

    def __str__(self) -> str:
        return self.color

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        app_label="shop"


class Products(models.Model):
    socket = models.ForeignKey(Socket, on_delete=models.SET_NULL, blank=True, null=True)
    switch = models.ForeignKey(Switch, on_delete=models.SET_NULL, blank=True, null=True)
    frame = models.ForeignKey(Frame, on_delete=models.SET_NULL, blank=True, null=True)
    plug = models.ForeignKey(Plug, on_delete=models.SET_NULL, blank=True, null=True)
    computer_socket = models.ForeignKey(ComputerSocket, on_delete=models.SET_NULL, blank=True, null=True)
    dimmer = models.ForeignKey(Dimmer, on_delete=models.SET_NULL, blank=True, null=True)
    thermostat = models.ForeignKey(Thermostat, on_delete=models.SET_NULL, blank=True, null=True)
    network_filter = models.ForeignKey(NetworkFilter, on_delete=models.SET_NULL, blank=True, null=True)
