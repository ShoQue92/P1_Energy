from functions import str_naar_dt
from functions import print_gas_meting
from functions import opvragen_data
from functions import list_to_dict_convert
from functions import tabel_naam_via_IP
from functions import meter_IP_via_naam
from functions import meter_naam_via_IP
from functions import handmatige_meting
from functions import interval_meting
from db_sdk import create_tables
from db_sdk import drop_tables
from db_sdk import insert_record
from datetime import datetime
from sys import argv

create_tables()

commands = {
       "handmatige_meting": handmatige_meting,
       "interval_meting": interval_meting
}

# bestandsnaam negeren
argv.pop(0)

if not argv:
       print("Geen commando meegegeven!")
       exit(1)

# eerste cmd argument is altijd de command
received_command = argv.pop(0)
# match command naar functie met de dictionary, bestaat deze niet dan krijgen we None terug
matched_command = commands.get(received_command)

#check of command bestaat, als dat het geval is roep deze aan met de rest van de argumenten
if not matched_command:
       print("Geen geldig commando gevonden.")
       exit(1)

matched_command(*argv)
exit(0)