#!/usr/bin/python

# This script reads a DHT22 sensor and pushes the values to a dummy device in FHEM

import sys
import Adafruit_DHT
import requests

sensor = Adafruit_DHT.DHT22 # might be also DHT11 or AM2301
pin = 4 		# GPIO pin
ip = '192.168.178.40'	# IP of FHEM
port = '8083'		# Port of FHEM
FhemDevice = 'DHT22'	# Name of Device in FHEM

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=setreading%20'+FhemDevice+'%20temperature%20' + str(round(temperature,1)))
	r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=setreading%20'+FhemDevice+'%20humidity%20' + str(round(humidity,0)))
	r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=set%20'+FhemDevice+'%20Temp:%20' + str(round(temperature,1)) + '%20Hum: ' + str(round(humidity,0)))
else:
	print('Reading failed. Please check connectivity of sensor.')
	sys.exit(1)
