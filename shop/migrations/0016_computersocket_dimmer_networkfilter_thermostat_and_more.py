# Generated by Django 4.0.1 on 2022-02-15 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_plug_plugcolor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerSocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('computer_socket_type', models.CharField(max_length=40, verbose_name='Тип')),
                ('montage', models.CharField(max_length=20, verbose_name='Монтаж')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='computer_socket_images', verbose_name='Изображение')),
                ('rated_current', models.CharField(max_length=20, verbose_name='Номинальный ток')),
                ('socket', models.CharField(max_length=20, verbose_name='Розетка')),
                ('grounding', models.BooleanField(default=True, verbose_name='Заземление')),
                ('protection', models.CharField(max_length=20, verbose_name='Пылевлагозащищенность')),
                ('kids_protection', models.BooleanField(blank=True, verbose_name='Защита от детей')),
                ('material', models.CharField(max_length=20, verbose_name='Материал')),
            ],
            options={
                'verbose_name': 'Компьютерная розетка',
                'verbose_name_plural': 'Компьютерные розетки',
            },
        ),
        migrations.CreateModel(
            name='Dimmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('dimmer_type', models.CharField(max_length=20, verbose_name='Тип')),
                ('montage', models.CharField(max_length=20, verbose_name='Монтаж')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='dimmer_images', verbose_name='Изображение')),
                ('terminal', models.CharField(max_length=20, verbose_name='Клемма')),
                ('grounding', models.BooleanField(default=True, verbose_name='Заземление')),
                ('three_phase_socket', models.BooleanField(default=False, verbose_name='Трехфазная розетка')),
                ('control', models.CharField(max_length=60, verbose_name='Управление')),
                ('protection', models.CharField(max_length=20, verbose_name='Пылевлагозащищенность')),
                ('kids_protection', models.BooleanField(blank=True, verbose_name='Защита от детей')),
                ('backlight', models.BooleanField(default=False, verbose_name='Подсветка')),
                ('peculiarities', models.CharField(max_length=60, verbose_name='Особенности')),
                ('material', models.CharField(max_length=20, verbose_name='Материал')),
                ('equipment', models.CharField(max_length=60, verbose_name='Комплектация')),
                ('width', models.IntegerField(default=0, verbose_name='Ширина')),
                ('height', models.IntegerField(default=0, verbose_name='Высота')),
                ('depth', models.IntegerField(default=0, verbose_name='Глубина')),
            ],
            options={
                'verbose_name': 'Диммер',
                'verbose_name_plural': 'Диммеры',
            },
        ),
        migrations.CreateModel(
            name='NetworkFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('network_filter_type', models.CharField(max_length=30, verbose_name='Тип')),
                ('output_sockets', models.CharField(max_length=30, verbose_name='Выходные розетки')),
                ('total_number_of_outlets', models.IntegerField(default=4, verbose_name='Общее количество выходных розеток')),
                ('input_socket', models.CharField(max_length=30, verbose_name='Входная розетка')),
                ('avr', models.BooleanField(default=False, verbose_name='Автоматическая стабилизация напряжения')),
                ('power_cable', models.IntegerField(default=5, verbose_name='Кабель питания, м.')),
                ('protective_shutters', models.BooleanField(default=False, verbose_name='Защитные шторки/крышки на розетках')),
                ('separate_switches', models.BooleanField(default=False, verbose_name='Раздельные выключатели')),
                ('nineteen_rack_mounting', models.BooleanField(default=False, verbose_name="Монтаж в 19' стойку")),
                ('wall_mount', models.BooleanField(default=False, verbose_name='Крепление к стене')),
                ('rated_current', models.CharField(max_length=20, verbose_name='Номинальное входное напряжение')),
                ('max_input_pulse_energy', models.CharField(max_length=20, verbose_name='Макс. энергия входного импульса')),
                ('max_load_current', models.CharField(max_length=20, verbose_name='Макс. ток нагрузки')),
                ('communication_line_protection', models.BooleanField(default=False, verbose_name='Защита линий связи')),
                ('indication', models.CharField(max_length=60, verbose_name='Индикация')),
                ('usb_ports', models.CharField(blank=True, max_length=20, verbose_name='Usb-порты')),
                ('overheat_protection', models.BooleanField(default=False, verbose_name='Защита от перегрева')),
                ('load_short_circuit_protection', models.BooleanField(default=False, verbose_name='Защита от КЗ')),
                ('over_voltage_protection', models.BooleanField(default=False, verbose_name='Защита от повышения напряжения')),
                ('remote_control', models.BooleanField(blank=True, verbose_name='Пульт ДУ')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='networkfilter_images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Сетевой фильтр',
                'verbose_name_plural': 'Сетевые фильтры',
            },
        ),
        migrations.CreateModel(
            name='Thermostat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Название')),
                ('slug', models.SlugField(max_length=60, unique=True, verbose_name='Ссылка')),
                ('code', models.CharField(max_length=20, verbose_name='Код')),
                ('description', models.TextField(verbose_name='Описание')),
                ('manufacturer', models.CharField(blank=True, default='Schneider Electric', max_length=60, null=True, verbose_name='Производитель')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Стоимость')),
                ('stock', models.IntegerField(default=0, verbose_name='Количество')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие')),
                ('thermostat_type', models.CharField(max_length=30, verbose_name='Тип')),
                ('appointment', models.CharField(max_length=60, verbose_name='Назначение')),
                ('control', models.CharField(max_length=60, verbose_name='Управление')),
                ('display', models.CharField(max_length=60, verbose_name='Экран')),
                ('air_temperature_sensor', models.BooleanField(blank=True, verbose_name='Датчик температуры воздуха')),
                ('floor_temperature_sensor', models.BooleanField(blank=True, verbose_name='Датчик температуры пола')),
                ('remote_control', models.BooleanField(blank=True, verbose_name='Пульт ДУ')),
                ('montage', models.CharField(max_length=20, verbose_name='Монтаж')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='thermostat_images', verbose_name='Изображение')),
                ('temperature_range', models.CharField(max_length=60, verbose_name='Диапазон температур')),
                ('remote_sensor_wire_length', models.IntegerField(default=3, verbose_name='Длина провода выносного датчика')),
            ],
            options={
                'verbose_name': 'Терморегулятор',
                'verbose_name_plural': 'Терморегуляторы',
            },
        ),
        migrations.CreateModel(
            name='ThermostatColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='networkfilter_images', verbose_name='Изображение')),
                ('network_filter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.networkfilter', verbose_name='Сетевой фильтр')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='DimmerColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='dimmer_images', verbose_name='Изображение')),
                ('dimmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.dimmer', verbose_name='Диммер')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
        migrations.CreateModel(
            name='ComputerSocketColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=60, verbose_name='Цвет')),
                ('color_code', models.CharField(default='#fff', max_length=60, verbose_name='Код цвета')),
                ('image', models.ImageField(upload_to='computer_socket_images', verbose_name='Изображение')),
                ('computer_socket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='color', to='shop.computersocket', verbose_name='Компьютерная розетка')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
            },
        ),
    ]
