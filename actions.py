import requests
from functions import str_naar_dt
from functions import print_gas_meting
from functions import opvragen_data_van_p1

IP = '192.168.1.213'

data = opvragen_data_van_p1(IP)

#meter informatie
meter_type = data['meter_model']
meter_smr_version = data['smr_version']
meter_connected_to_wifi_ssid = data['total_gas_m3']
wifi_strength = data['wifi_strength']

# stroom informatie
stroomimport_dal = data['total_power_import_t1_kwh']
stroomimport_normaal = data['total_power_import_t2_kwh']
active_power_w = data['active_power_w']
active_power_l1_w = data['active_power_l1_w']

# gas informatie
total_gas_m3 = data['total_gas_m3']
gas_measurement_timestamp_int = data['gas_timestamp']
gas_measurement_timestamp_str = str(gas_measurement_timestamp_int)
gas_measurement_timestamp_dt = str_naar_dt(gas_measurement_timestamp_str, '%y%m%d%H%M%S')
   

print(active_power_l1_w)
#print_gas_meting(total_gas_m3, gas_measurement_timestamp_dt)