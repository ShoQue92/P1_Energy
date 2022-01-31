FROM python:3.10-slim

RUN mkdir -p /home/p1_energy
WORKDIR /home/p1_energy

RUN pip install -U python-dotenv
RUN pip install -U requests

COPY . /home/p1_energy
CMD  [ "python", "actions.py","interval_meting","woonkamer_metingen","192.168.1.204","1" ]
