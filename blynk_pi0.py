import blynklib
from w1thermsensor import W1ThermSensor
#import RPi.GPIO as GPIO
from Adafruit_IO import Client, Feed, Data, RequestError

ADAFRUIT_IO_KEY = 'xxxxx'
ADAFRUIT_IO_USERNAME = 'xxxxx'

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
try:
        temperature1= aio.feeds('temperature1')
        temperature2= aio.feeds('temperature2')
except RequestError:
        feed1= Feed(name="temperature1")
        temperature1 = aio.create_feed(feed1)

        feed2= Feed(name="temperature2")
        temperature2 = aio.create_feed(feed2)




#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.OUT)
#GPIO.setup(4, GPIO.IN)

#GPIO.output(4, GPIO.LOW)

#from w1thermsensor import AsyncW1ThermSensor, Unit

#  1. HWID: 8a2017ed14ff Type: DS18B20
#  2. HWID: 8a2017e53fff Type: DS18B20

# DS18B20
temp_1_id = "8a2017e53fff"
temp_1_pin = 4

# DS18B20
temp_2_id = "8a2017ed14ff"
temp_2_pin = 5


def readProbe(sensor_id):
        try:
                sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, sensor_id)
                temperature_c = sensor.get_temperature()
                print("The temperature is %s celsius" % temperature_c)
                temperature_f = temperature_c * 9.0 / 5.0 + 32.0
                print("The temperature is %s f" % temperature_f)
        except:
                print("Sensor not found")
                temperature_f = 32
                pass
        return(temperature_f)

def connectBlynk(auth_key):
        blynk = blynklib.Blynk(auth_key)
        blynk.run()
        return(blynk)

def writeValue(blynk_conn, pin, value):
        blynk_conn.virtual_write(pin, value)


BLYNK_AUTH = "xxxxx"

blynk_c = connectBlynk(BLYNK_AUTH)

temp_1_value = readProbe(temp_1_id)
writeValue(blynk_c, temp_1_pin, temp_1_value)
aio.send_data(temperature1.key, temp_1_value)

temp_2_value = readProbe(temp_2_id)
writeValue(blynk_c, temp_2_pin, temp_2_value)
aio.send_data(temperature2.key, temp_2_value)
