	
import sys
import urllib.request
from time import sleep
import Adafruit_DHT as dht
import logging
import json
from pprint import pprint

# To avoid the error on rc.local execution envirotment: 
#WARNING urllib3.connectionpool Retrying (Retry(total=2, connect=None, read=None, redirect=None, status=None)) after connection broken by 'NewConnectionError('<urllib3.connection
logging.getLogger("urllib3").setLevel(logging.ERROR)

# Then the code sets up the logging module. We are going to use the basicConfig() function to set up the default handler 
# so that any debug messages are written to the file /home/pi/event_error.log.
logging.basicConfig(filename='humidity_event_error.log',
  level=logging.DEBUG,
  format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

# Read the configuration file
DEFAULT_CONFIG_PATH = 'config.json'

while True:
        try:
                with open(DEFAULT_CONFIG_PATH, 'r') as config_file:
                	config = json.load(config_file)

                	# URL where we will send the data,
                	baseURL = 'https://api.thingspeak.com/update?api_key=%s' % config['domohome_livingroom_humidity']['write_api_key']

                	def DHT22_data():
                        	# Reading from DHT22 and storing the temperature and humidity
                        	humi, temp = dht.read_retry(dht.DHT22, config['domohome_livingroom_humidity']['gpio_pin'])
                        	return humi, temp

                	humi, temp = DHT22_data()

                	# If Reading is valid
                	if isinstance(humi, float) and isinstance(temp, float):
                        	# Formatting to two decimal places
                        	humi = '%.2f' % humi
                       		temp = '%.2f' % temp
                        	print (humi)
                        	print (temp)


                        	# Sending the data to thingspeak
                        	request = urllib.request.Request(baseURL + '&field1=%s&field2=%s' % (temp, humi))
                        	response = urllib.request.urlopen(request)
                        	print (response.read().decode('utf-8'))
                		# Closing the connection
                        	conn.close()

                	else:
                        	print ("Sensor reading error")

                	# DHT22 requires 2 seconds to give a reading, so make sure to add delay of above 2 seconds.
                	sleep(20000)

        except Exception as e:
                pprint("Exception reading and sendinf data: %s\n" % e)
                logger.error("Exception reading and sendinf data: %s\n" % e)
