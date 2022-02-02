from datetime import datetime
import requests
import time 
from influx import influx_point
import os

IP = os.environ['DEVICE_IP']
BRON = os.environ['DEVICE_BRON']

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

def main():
    print('Meting gestart!')
    i = 1
    while True:
        match BRON:
            case 'meterkast':
                data = opvragen_data(IP) 
                print(BRON, 'meting', '[',i,']', '@', '[',data['timestamp'],']:', '--> active_power_w:',data['active_power_w'], ', active_power_l1_w:', data['active_power_l1_w'], ', total_gas_m3: ', data['total_gas_m3'])
                influx_point(BRON, data)
                print('Meting','[',i,']','succesvol gelogd in Influx!')
                i += 1

            case 'woonkamer':
                data = opvragen_data(IP) 
                print(BRON, 'meting', '[', i,']', '@', '[', data['timestamp'],']:', '--> active_power_w:',data['active_power_w'], ', active_power_l1_w:', data['active_power_l1_w'])
                influx_point(BRON, data)
                print('Meting', '[', i, ']','succesvol gelogd in Influx!')
                i += 1

            case 'kantoor':
                data = opvragen_data(IP) 
                print(BRON, 'meting', '[', i,']', '@', '[', data['timestamp'],']:', '--> active_power_w:',data['active_power_w'], ', active_power_l1_w:', data['active_power_l1_w'])
                influx_point(BRON, data)
                print('Meting', '[', i, ']','succesvol gelogd in Influx!')
                i += 1
main()