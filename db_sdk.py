import sqlite3
import os
from os.path import join, dirname
from dotenv import load_dotenv
import traceback
import time
import sys

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# gebruiken we overal dus global
db_path =  os.environ.get("DB_PATH")
db_name =  os.environ.get("DB_NAME")

conn = sqlite3.connect(db_path + db_name)
c = conn.cursor()

def create_tables():
    sql_statement_meterkast = 'CREATE TABLE IF NOT EXISTS ' +  'meterkast_metingen' + '(' + 'smr_version TEXT, meter_model TEXT, wifi_ssid TEXT, wifi_strength REAL, total_power_import_t1_kwh REAL, total_power_import_t2_kwh REAL, total_power_export_t1_kwh REAL, total_power_export_t2_kwh REAL, active_power_w REAL, active_power_l1_w REAL, active_power_l2_w REAL, active_power_l3_w REAL, total_gas_m3 REAL, gas_timestamp DATE, timestamp TEXT'  + ')'
    sql_statement_kantoor = 'CREATE TABLE IF NOT EXISTS ' +  'kantoor_metingen' + '(' + 'wifi_ssid TEXT, wifi_strength TEXT, total_power_import_t1_kwh REAL, total_power_export_t1_kwh REAL, active_power_w REAL, active_power_l1_w REAL, timestamp TEXT'  + ')'
    sql_statement_woonkamer = 'CREATE TABLE IF NOT EXISTS ' +  'woonkamer_metingen' + '(' + 'wifi_ssid TEXT, wifi_strength TEXT, total_power_import_t1_kwh REAL, total_power_export_t1_kwh REAL, active_power_w REAL, active_power_l1_w REAL, timestamp TEXT'  + ')'
    print('Tabellen worden aangemaakt'.center(100,'='))
    try:
        c.execute(sql_statement_meterkast)
        print('Aanmaken meterkast_metingen'.center(50,'.'))
        c.execute(sql_statement_kantoor)
        print('Aanmaken kantoor_metingen'.center(50,'.'))
        c.execute( sql_statement_woonkamer)
        print('Aanmaken woonkamer_metingen'.center(50,'.'))
        print('Tabellen succesvol aangemaakt'.center(100,'='))
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))
    
def drop_tables():
    sql_statement_meterkast = 'DROP TABLE  ' +  'meterkast_metingen' 
    sql_statement_kantoor = 'DROP TABLE ' +  'kantoor_metingen' 
    sql_statement_woonkamer = 'DROP TABLE ' +  'woonkamer_metingen' 
    print('Tabellen worden gedropt'.center(100,'='))
    try:
        c.execute(sql_statement_meterkast)
        print('Droppen meterkast_metingen'.center(50,'.'))
        c.execute(sql_statement_kantoor)
        print('Droppen kantoor_metingen'.center(50,'.'))
        c.execute( sql_statement_woonkamer)
        print('Droppen woonkamer_metingen'.center(50,'.'))
        print('Tabellen succesvol gedropt'.center(100,'='))
    except sqlite3.Error as er:
        print('SQLite error: %s' % (' '.join(er.args)))
        print("Exception class is: ", er.__class__)
        print('SQLite traceback: ')
        exc_type, exc_value, exc_tb = sys.exc_info()
        print(traceback.format_exception(exc_type, exc_value, exc_tb))

def insert_record(table, columns, values):
    match table:
        case "meterkast_metingen":
            #print('meterkast')
            sql_statement = 'INSERT INTO ' + table + ' ( ' + ', '.join(str(v) for v in columns) + ' ) ' + 'VALUES' + ' ( ' + ', '.join('\'' + str(v) + '\'' for v in values) + ' ) '
            c.execute( sql_statement)
            conn.commit()
        case "kantoor_metingen":
            #print('kantoor')
            sql_statement = 'INSERT INTO ' + table + ' ( ' + ', '.join(str(v) for v in columns) + ' ) ' + 'VALUES' + ' ( ' + ', '.join('\'' + str(v) + '\'' for v in values) + ' ) '
            c.execute( sql_statement)
            conn.commit()
        case "woonkamer_metingen":
            #print('woonkamer')
            sql_statement = 'INSERT INTO ' + table + ' ( ' + ', '.join(str(v) for v in columns) + ' ) ' + 'VALUES' + ' ( ' + ', '.join('\'' + str(v) + '\'' for v in values) + ' ) '
            #print(sql_statement)
            c.execute( sql_statement)
            conn.commit()
        case _:
            print('Geen geldige tabel opgegeven!')