import sys
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None:
     print('{0:0.2f}'.format(humidity))
else:
     print('Failed to get reading. Try again!')
     sys.exit(1)