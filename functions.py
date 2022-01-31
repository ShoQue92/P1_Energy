from datetime import datetime
import requests
import time 
from db_sdk import create_tables
from db_sdk import drop_tables
from db_sdk import insert_record

from influxdb import influx_loggen

def opvragen_data(IP):
    URL = 'http://'+IP+'/api/v1/data'
    r = requests.get(url=URL)
    result = r.raise_for_status()
    base_result =  r.json()
    #Ophalen huidige timestamp en toevoegen als element in de dictionary
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    base_result.update({'timestamp': current_timestamp })
    time.sleep(1)
    return base_result

def str_naar_dt(string, format):
    converted_string =  datetime.strptime(string, format)
    return converted_string

def print_gas_meting(meting, meetmoment):
    return print(f'{meting}m³, gemeten op {meetmoment}.')

def list_to_dict_convert(tuple):
    di = dict(tuple)
    return di

def tabel_naam_via_IP(IP):
    meters = {
        "meterkast_metingen" : "192.168.1.211",
        "kantoor_metingen" : "192.168.1.74",
        "woonkamer_metingen" : "192.168.1.204"
    }
    tabel_naam =  [key for key ,value  in meters.items() if value == IP]
    return tabel_naam[0]

def meter_IP_via_naam(naam):
    meters = {
        "meterkast_metingen" : "192.168.1.211",
        "kantoor_metingen" : "192.168.1.74",
        "woonkamer_metingen" : "192.168.1.204"
    }
    IP =  [value for key ,value  in meters.items() if key == naam]
    return IP[0]

def meter_naam_via_IP(IP):
    meters = {
        "meterkast_metingen" : "192.168.1.211",
        "kantoor_metingen" : "192.168.1.74",
        "woonkamer_metingen" : "192.168.1.204"
    }
    naam =  [key for key ,value  in meters.items() if value == IP]
    return naam[0]

def handmatige_meting(naam,IP, duur):
    print('Starten meting voor ' + meter_naam_via_IP(IP) + ' op ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' voor de duur van ' + str(duur) + ' seconden')
    i = 0
    while True:
        data = opvragen_data(IP)
        insert_record(tabel_naam_via_IP(IP), list(data.keys()), list(data.values()))
        i +=1
        print(i)
        if i == duur:
            break

def interval_meting(naam,IP, interval=60):
    print('Starten meting voor ' + meter_naam_via_IP(IP) + ' op ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' in een interval van ' + str(interval) + ' seconden')
    i = 0
    while True:
        data = opvragen_data(IP)
        insert_record(tabel_naam_via_IP(IP), list(data.keys()), list(data.values()))
        time.sleep(int(interval))
        print_string = ' Meting iteratie ' + str(i) + ' voor ' + naam + ' '
        print(print_string.center(100,'='))
        i +=1
