from rest_framework import serializers
from .models import category_models
from .models import brand_models
from .models import collection_models
from .models import product_models


# Third Level Category

class ThirdLevelCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = category_models.ThirdLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Second Level Category

class SecondLevelCategorySerializer(serializers.ModelSerializer):

    category = ThirdLevelCategorySerializer(many=True)

    class Meta:
        model = category_models.SecondLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# First Level Category

class FirstLevelCategorySerializer(serializers.ModelSerializer):
    category = SecondLevelCategorySerializer(many=True)

    class Meta:
        model = category_models.FirstLevelCategory
        fields = ('__all__')
        lookup_field = 'slug'


# Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = brand_models.Brand
        fields = ('__all__')
        lookup_field = 'slug'


# Collection

class CollectionColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = collection_models.CollectionColor
        fields = ('color', 'image')


class CollectionOfferSerializer(serializers.ModelSerializer):
    collection = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')

    class Meta:
        model = collection_models.CollectionOffer
        fields = ('__all__')
        lookup_field = 'slug'


class CollectionSerializer(serializers.ModelSerializer):
    coolection_offer = CollectionOfferSerializer()
    color = CollectionColorSerializer(many=True)
    sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    switches = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    plugs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    frames = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    computer_sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    dimmers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    thermostats = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    network_filters = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')


    class Meta:
        model = collection_models.Collection
        fields = ('__all__')
        lookup_field = 'slug'


class ProductOfferSerializer(serializers.ModelSerializer):
    sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    switches = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    plugs = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    frames = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    computer_sockets = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    dimmers = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    thermostats = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    network_filters = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')                                                         

    class Meta:
        model = product_models.ProductOffer
        fields = ('__all__')
        lookup_field = 'slug'


# Socket

class SocketColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SocketColor
        fields = ('color', 'image')


class SocketSerializer(serializers.ModelSerializer):
    color = SocketColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'socket_type': obj.socket_type,
            'montage': obj.montage,
            'terminal': obj.terminal,
            'rated_current': obj.rated_current,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'socket': obj.socket,
            'grounding': obj.grounding,
            'protection': obj.protection,
            'kids_protection': obj.kids_protection,
            'backlight': obj.backlight,
            'material': obj.material,
            'equipment': obj.equipment,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.Socket
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# Switch

class SwitchColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.SwitchColor
        fields = ('color', 'image')


class SwitchSerializer(serializers.ModelSerializer):
    color = SwitchColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'switch_type': obj.switch_type,
            'montage': obj.montage,
            'terminal': obj.terminal,
            'rated_current': obj.rated_current,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'control': obj.control,
            'frame_places': obj.frame_places,
            'protection': obj.protection,
            'backlight': obj.backlight,
            'material': obj.material,
            'equipment': obj.equipment,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.Switch
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# Frame

class FrameColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.FrameColor
        fields = ('color', 'image')


class FrameSerializer(serializers.ModelSerializer):
    color = FrameColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'switch_type': obj.frame_type,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'frame_places': obj.frame_places,
            'material': obj.material,
            'equipment': obj.equipment,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.Frame
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# Plug

class PlugColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.PlugColor
        fields = ('color', 'image')


class PlugSerializer(serializers.ModelSerializer):
    color = PlugColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'plug_type': obj.plug_type,
            'montage': obj.montage,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'protection': obj.protection,
            'backlight': obj.backlight,
            'peculiarities': obj.peculiarities,
            'material': obj.material,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.Plug
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# ComputerSocket

class ComputerSocketColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ComputerSocketColor
        fields = ('color', 'image')


class ComputerSocketSerializer(serializers.ModelSerializer):
    color = ComputerSocketColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'computer_socket_type': obj.computer_socket_type,
            'montage': obj.montage,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'socket': obj.socket,
            'grounding': obj.grounding,
            'protection': obj.protection,
            'kids_protection': obj.kids_protection,
            'material': obj.material,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.ComputerSocket()
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# Dimmer

class DimmerColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.DimmerColor
        fields = ('color', 'image')


class DimmerSerializer(serializers.ModelSerializer):
    color = DimmerColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    proportions = serializers.SerializerMethodField('get_proportions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'dimmer_type': obj.dimmer_type,
            'montage': obj.montage,
            'terminal': obj.terminal,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'grounding': obj.grounding,
            'three_phase_socket': obj.three_phase_socket,
            'control': obj.control,
            'protection': obj.protection,
            'kids_protection': obj.kids_protection,
            'backlight': obj.backlight,
            'peculiarities': obj.peculiarities,
            'material': obj.material,
            'equipment': obj.equipment,
        }

    def get_proportions(self, obj):
        return {
            'width': obj.width,
            'height': obj.height,
            'depth': obj.depth,
        }

    class Meta:
        model = product_models.Dimmer()
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'proportions', 
        )
        lookup_field = 'slug'


# Thermostat

class ThermostatColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = product_models.ThermostatColor
        fields = ('color', 'image')


class ThermostatSerializer(serializers.ModelSerializer):
    color = ThermostatColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')
    programm_functions = serializers.SerializerMethodField('get_programm_functions')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'thermostat_type': obj.thermostat_type,
            'montage': obj.montage,
            'appointment': obj.appointment,
            'control': obj.control,
            'display': obj.display,
            'is_smart_home_system_device': obj.is_smart_home_system_device,
            'air_temperature_sensor': obj.air_temperature_sensor,
            'floor_temperature_sensor': obj.floor_temperature_sensor,
            'wi_fi_control': obj.wi_fi_control,
            'remote_control': obj.remote_control,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'remote_sensor_wire_length': obj.remote_sensor_wire_length,
            'temperature_hysteresis': obj.temperature_hysteresis,
            'maximum_load_current': obj.maximum_load_current,
            'maximum_load_power': obj.maximum_load_power,
            'correction_of_sensor_readings': obj.correction_of_sensor_readings,
            'sensor_connection_diagnostics': obj.sensor_connection_diagnostics,
            'protection_class': obj.protection_class,
        }

    def get_programm_functions(self, obj):
        return {
            'kids_protection': obj.kids_protection,
            'num_of_programs': obj.num_of_programs,
            'num_of_intervals_per_day': obj.num_of_intervals_per_day,
            'adaptive_function': obj.adaptive_function,
            'manual_mode': obj.manual_mode,
            'calculation_of_consumed_energy': obj.calculation_of_consumed_energy,
        }

    class Meta:
        model = product_models.Thermostat()
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
            'programm_functions', 
        )
        lookup_field = 'slug'


# NetworkFilter

class NetworkFilterColorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product_models.NetworkFilterColor
        fields = ('color', 'image')


class NetworkFilterSerializer(serializers.ModelSerializer):
    color = NetworkFilterColorSerializer(many=True)
    category = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    collection = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    product_offer = serializers.SlugRelatedField(read_only=True, slug_field='slug')
    manufacturer = serializers.SlugRelatedField(read_only=True, slug_field='slug')

    general = serializers.SerializerMethodField('get_general')
    basic = serializers.SerializerMethodField('get_basic')
    informational = serializers.SerializerMethodField('get_informational')
    technical = serializers.SerializerMethodField('get_technical')

    def get_general(self, obj):
        return {
            'name': obj.name,
            'slug': obj.slug,
            'code': obj.code,
            'description': obj.description,
        }

    def get_basic(self, obj):
        return {
            'network_filter_type': obj.network_filter_type,
            'output_sockets': obj.output_sockets,
            'total_number_of_outlets': obj.total_number_of_outlets,
            'input_socket': obj.input_socket,
            'avr': obj.avr,
            'power_cable': obj.power_cable,
            'protective_shutters': obj.protective_shutters,
            'separate_switches': obj.separate_switches,
            'remote_control_wi_fi': obj.remote_control_wi_fi,
            'nineteen_rack_mounting': obj.nineteen_rack_mounting,
            'wall_mount': obj.wall_mount,
        }
    
    def get_informational(self, obj):
        return {
            'price': obj.price,
            'stock': obj.stock,
            'availability': obj.availability,
        }

    def get_technical(self, obj):
        return {
            'rated_current': obj.rated_current,
            'max_input_pulse_energy': obj.max_input_pulse_energy,
            'max_load_current': obj.max_load_current,
            'communication_line_protection': obj.communication_line_protection,
            'indication': obj.indication,
            'usb_ports': obj.usb_ports,
            'overheat_protection': obj.overheat_protection,
            'load_short_circuit_protection': obj.load_short_circuit_protection,
            'over_voltage_protection': obj.over_voltage_protection,
            'remote_control': obj.remote_control,
        }

    class Meta:
        model = product_models.NetworkFilter()
        fields = (
            'id',
            'type_of',
            'thumbnail', 
            'color', 
            'manufacturer', 
            'product_offer', 
            'category', 
            'collection', 
            'general', 
            'basic', 
            'informational', 
            'technical', 
        )
        lookup_field = 'slug'
