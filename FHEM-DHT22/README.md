# DHT11/DHT22 FHEM Python Interface

This script reads a DHT11 or DHT22 device and pushes its temperature and humidity values to a FHEM dummy device 

Below is the manual to get everything setup. Please adjust parameters in FHEM_DHT22.py as required. The command line parameter defines the name of the dummy device in FHEM

' ./FHEM_DHT22.py <Name of Dummy Device>

# Install instructions

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install build-essential python-dev python-openssl

git clone https://github.com/adafruit/Adafruit_Python_DHT
cd Adafruit_Python_DHT/
python setup.py install
cd ..

git clone https://github.com/smarthomescripting/FHEM
cd FHEM
./FHEM_DHT22.py DHT22
```

# Add to crontab 

Add a line as follows

*/5 * * * * /home/FHEM/FHEM_DHT22.py DHT22
