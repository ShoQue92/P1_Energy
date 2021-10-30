from datetime import datetime
import requests

def opvragen_data(IP):
    URL = 'http://'+IP+'/api/v1/data'
    r = requests.get(url=URL)
    result = r.raise_for_status()
    base_result =  r.json()
    #Ophalen huidige timestamp en toevoegen als element in de dictionary
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    base_result.update({'timestamp': current_timestamp })
    return base_result

def str_naar_dt(string, format):
    converted_string =  datetime.strptime(string, format)
    return converted_string

def print_gas_meting(meting, meetmoment):
    return print(f'{meting}m³, gemeten op {meetmoment}.')

def list_to_dict_convert(tuple):
    di = dict(tuple)
    return di

def meter_naam_via_IP(IP):
    meters = {
        "meterkast_metingen" : "192.168.1.211",
        "kantoor_metingen" : "192.168.1.76",
        "woonkamer_metingen" : "192.168.1.206"
    }
    tabel_naam =  [key for key ,value  in meters.items() if value == IP]
    return tabel_naam[0]