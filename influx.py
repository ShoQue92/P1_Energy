from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

URL = 'http://192.168.1.2:8086'

token = "XOMsKupabsqnNqcjjmSWxcfk9UjXi2y6vZEjdImA4ugnAg6vamBcyk4rmMtZZUVgKhdJzqSv5LtWrUdfUAx6Gg=="
org = "brugts"
bucket = "energy"

client = InfluxDBClient(url=URL, token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

def influx_point(bron,data):

    point = Point(bron)\
    .tag("host", data['meter_model'])\
    .field("active_power_w", data['active_power_w'])\
    .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point(bron)\
    .tag("host", data['meter_model'])\
    .field("active_power_l1_w", data['active_power_l1_w'])\
    .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

    point = Point(bron)\
    .tag("host", data['meter_model'])\
    .field("total_gas_m3", data['total_gas_m3'])\
    .time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)