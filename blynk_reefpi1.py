import blynklib
from w1thermsensor import W1ThermSensor
#from w1thermsensor import AsyncW1ThermSensor, Unit

from Adafruit_IO import Client, Feed, Data, RequestError

ADAFRUIT_IO_KEY = 'xxxx'
ADAFRUIT_IO_USERNAME = 'xxxxx'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
        temperature3= aio.feeds('temperature3')
        temperature4= aio.feeds('temperature4')
except RequestError:
        feed3= Feed(name="temperature3")
        temperature3 = aio.create_feed(feed3)

        feed4= Feed(name="temperature4")
        temperature4 = aio.create_feed(feed4)


# DS18B20
temp_29 = "8a2017e4d6ff"
temp_29_pin = 4

temp_flex = "8a201812d1ff"
temp_flex_pin = 5

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, temp_29)
#
temperature_c = sensor.get_temperature()
print("The temperature is %s celsius" % temperature_c)
temperature_f = temperature_c * 9.0 / 5.0 + 32.0
print("The temperature is %s f" % temperature_f)
temp_29 = temperature_f

sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, temp_flex)
#
temperature_c = sensor.get_temperature()
print("The temperature is %s celsius" % temperature_c)
temperature_f = temperature_c * 9.0 / 5.0 + 32.0
print("The temperature is %s f" % temperature_f)
temp_flex = temperature_f


# BLYNK_AUTH = "xxxxx"
BLYNK_AUTH = "xxxxx"

blynk = blynklib.Blynk(BLYNK_AUTH)
blynk.run()


print("Writing to Blynk...")
blynk.virtual_write(temp_29_pin, temp_29)
aio.send_data(temperature3.key, temp_29)

blynk.virtual_write(temp_flex_pin, temp_flex)
aio.send_data(temperature4.key, temp_flex)
