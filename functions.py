from datetime import datetime
import requests

def opvragen_data_van_p1(IP):
    URL = 'http://'+IP+'/api/v1/data'
    r = requests.get(url=URL)
    result = r.raise_for_status()
    return r.json()

def str_naar_dt(string, format):
    converted_string =  datetime.strptime(string, format)
    return converted_string

def print_gas_meting(meting, meetmoment):
    return print(f'Stand gasmeter: {meting}.\nGemeten op {meetmoment}.')