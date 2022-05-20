from django_filters import rest_framework as filters
from .models import product_models


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SocketFilter(filters.FilterSet):
    price = filters.RangeFilter()
    rated_current = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter()

    class Meta:
        model = product_models.Socket
        fields = [
            'price', 
            'availability', 
            'manufacturer', 
            'socket_type', 
            'montage',
            'terminal',
            'rated_current',
            'grounding',
            'protection',
            'kids_protection',
            'backlight',
            'width',
            'height',
            'depth',
            'product_offer',
        ]


class SwitchFilter(filters.FilterSet):
    price = filters.RangeFilter()
    rated_current = filters.RangeFilter()
    frame_places = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter() 

    class Meta:
        model = product_models.Switch
        fields = [
            'price', 
            'availability', 
            'manufacturer', 
            'switch_type', 
            'montage',
            'terminal',
            'control',
            'rated_current',
            'protection',
            'frame_places',
            'backlight',
            'width',
            'height',
            'depth',
            'product_offer',
        ]


class FrameFilter(filters.FilterSet):
    price = filters.RangeFilter()
    frame_places = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter() 

    class Meta:
        model = product_models.Frame
        fields = [
            'price',
            'frame_places',
            'width',
            'height',
            'depth',
            'frame_type',
            'product_offer',
        ]


class PlugFilter(filters.FilterSet):
    price = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter() 

    class Meta:
        model = product_models.Plug
        fields = [
            'price',
            'width',
            'height',
            'depth',
            'plug_type',
            'montage',
            'backlight',
            'product_offer',
        ]


class ComputerSocketFilter(filters.FilterSet):
    rated_current = filters.RangeFilter()
    price = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter()
    
    class Meta:
        model = product_models.ComputerSocket
        fields = [
            'price',
            'width',
            'height',
            'depth',
            'computer_socket_type',
            'montage',
            'rated_current',
            'grounding',
            'kids_protection',
            'product_offer',
        ]


class DimmerFilter(filters.FilterSet):
    price = filters.RangeFilter()
    width = filters.RangeFilter()
    height = filters.RangeFilter()
    depth = filters.RangeFilter()

    class Meta:
        model = product_models.Dimmer
        fields = [
            'price',
            'width',
            'height',
            'depth',
            'dimmer_type',
            'montage',
            'terminal',
            'grounding',
            'three_phase_socket',
            'kids_protection',
            'backlight',
            'control',
            'product_offer',
        ]


class ThermostatFilter(filters.FilterSet):
    temperature_range = filters.RangeFilter()
    remote_sensor_wire_length = filters.RangeFilter()
    temperature_hysteresis = filters.RangeFilter()
    maximum_load_current = filters.RangeFilter()
    maximum_load_power = filters.RangeFilter()
    num_of_programs = filters.RangeFilter()
    num_of_intervals_per_day = filters.RangeFilter()
    price = filters.RangeFilter()

    class Meta:
        model = product_models.Thermostat
        fields = [
            'price',
            'thermostat_type',
            'is_smart_home_system_device',
            'control',
            'display',
            'air_temperature_sensor',
            'floor_temperature_sensor',
            'wi_fi_control',
            'remote_control',
            'montage',
            'temperature_range',
            'remote_sensor_wire_length',
            'temperature_hysteresis',
            'maximum_load_current',
            'maximum_load_power',
            'kids_protection',
            'num_of_programs',
            'num_of_intervals_per_day',
            'adaptive_function',
            'manual_mode',
            'calculation_of_consumed_energy',
            'product_offer',
        ]


class NetworkFilterFilter(filters.FilterSet):
    price = filters.RangeFilter()
    total_number_of_outlets = filters.RangeFilter()
    power_cable = filters.RangeFilter()
    rated_current = filters.RangeFilter()
    max_input_pulse_energy = filters.RangeFilter()
    max_load_current = filters.RangeFilter()
    usb_ports = filters.RangeFilter()

    class Meta:
        model = product_models.NetworkFilter
        fields = [
            'price',
            'network_filter_type',
            'total_number_of_outlets',
            'avr',
            'power_cable',
            'protective_shutters',
            'separate_switches',
            'remote_control_wi_fi',
            'nineteen_rack_mounting',
            'wall_mount',
            'rated_current',
            'max_input_pulse_energy',
            'max_load_current',
            'communication_line_protection',
            'usb_ports',
            'overheat_protection',
            'load_short_circuit_protection',
            'over_voltage_protection',
            'remote_control',
            'product_offer',
        ]