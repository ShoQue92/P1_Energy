from functions import str_naar_dt
from functions import print_gas_meting
from functions import opvragen_data
from functions import list_to_dict_convert
from functions import tabel_naam_via_IP
from functions import meter_IP_via_naam
from functions import meter_naam_via_IP
from db_sdk import create_tables
from db_sdk import drop_tables
from db_sdk import insert_record
from datetime import datetime

IP = '192.168.1.206'

def starten_meting(naam,duur):
    print('Starten meting voor ' + meter_naam_via_IP(IP) + ' op ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + 'voor de duur van ' + str(duur) + ' seconden')
    i = 0
    while True:
        data = opvragen_data(IP)
        insert_record(tabel_naam_via_IP(IP), list(data.keys()), list(data.values()))
        i +=1
        print(i)
        if i == duur:
            break

starten_meting('meterkast',60)