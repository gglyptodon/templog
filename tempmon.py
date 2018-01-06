#import Adafruit_DHT

#SENSOR = Adafruit_DHT.DHT22
#PIN =  4


def get_hum_temp():
    #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    humidity, temperature = 40,22 # dummy
    return humidity, temperature