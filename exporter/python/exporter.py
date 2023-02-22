# -*- coding: utf-8 -*-
import requests
import json
import time
from prometheus_client import start_http_server, Gauge

url_numero_pessoas = "http://api.open-notify.org/astros.json"
url_local_ISS = "http://api.open-notify.org/iss-now.json"

def pega_local_ISS():
    try:
        response = requests.get(url_local_ISS)
        data = response.json()
        return data['iss_position']
    except Exception as E:
        print("Erro para acessar URL")
        raise E

def pega_numero_astronautas():
    try:
        response = requests.get(url_numero_pessoas)
        data = response.json()
        return data['number']
    except Exception as E:
        print("Erro para acessar URL")
        raise E

def atualiza_metricas():
    try:
        numero_pessoas = Gauge('numero_de_autronautas', 'Numero de austronautas no espaço')
        longitude_iss = Gauge('longitude_iss', 'Longitude atual da ISS')
        latitude_iss = Gauge('latitude_iss', 'Latitude atual da ISS')
        while True:
            numero_pessoas.set(pega_numero_astronautas())
            latitude_iss.set(pega_local_ISS()['latitude'])
            longitude_iss.set(pega_local_ISS()['longitude'])
            time.sleep(10)
    except Exception as E:
        print("Erro para atualizar valor")
        raise E

def inicia_exporter():
    try:
        start_http_server(8899)
        return True
    except Exception as e:
        print("Problemas para iniciar exporter")
        raise e

def main():
    try:
        inicia_exporter()
        print("HTTP Server Iniciado")
        atualiza_metricas()
    except Exception as E:
        print("Problemas na inicialização do exporter")
        exit(1)

if __name__ == '__main__':
    main()
    exit(0)
