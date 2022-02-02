FROM python:3.10-slim

RUN mkdir -p /home/p1_energy
WORKDIR /home/p1_energy

RUN pip install -U requests
RUN pip install -U influxdb_client

COPY . /home/p1_energy/
CMD  [ "python3", "functions.py" ]
