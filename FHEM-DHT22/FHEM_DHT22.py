#!/usr/bin/python

# This script reads a DHT22 sensor and pushes the values to a dummy device in FHEM

import sys
import Adafruit_DHT
import requests
import os
import os.path

sensor = Adafruit_DHT.DHT22 # might be also DHT11 or AM2301
pin = 4 		# GPIO pin
ip = '192.168.178.40'	# IP of FHEM
port = '8083'		# Port of FHEM
FhemDevice = sys.argv[1]	# Name of Device in FHEM (taken from command line parameters)

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:

	filename= os.path.dirname(os.path.realpath(__file__)) + os.sep + 'history.dat'
	
	if os.path.exists(filename):
		file = open(filename, 'r')
        	old_temp = float(file.readline())
        	old_hum = float(file.readline())
        	file.close()
	else:
		old_temp = temperature
		old_hum = humidity

	if (temperature / old_temp) < 1.2 and (temperature / old_temp) > 0.8 and (humidity / old_hum) < 1.2 and (humidity / old_hum) > 0.8:
 	
		file = open(filename, 'w+')
        	file.truncate()
        	file.write(str(round(temperature,1)))
        	file.write("\n")
        	file.write(str(round(humidity,1)))
        	file.close()
		
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
		r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=setreading%20'+FhemDevice+'%20temperature%20' + str(round(temperature,1)))
		r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=setreading%20'+FhemDevice+'%20humidity%20' + str(round(humidity,0)))
		r = requests.get('http://' + ip + ':' + port + '/fhem?cmd.dummy=set%20'+FhemDevice+'%20Temp:%20' + str(round(temperature,1)) + '%20Hum: ' + str(round(humidity,0)))
	else:
		print('Ignoring exceptional values')
        	sys.exit(1)
else:
	print('Reading failed. Please check connectivity of sensor.')
	sys.exit(1)
