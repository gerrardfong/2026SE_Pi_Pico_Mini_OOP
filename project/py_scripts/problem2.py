from machine import Pin 
from time import sleep

sleep(0.1)

led_pin = 25
led2_pin = 15
data_pin = 13

led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

data = Pin(data_pin, Pin.IN)

while True:
    if data.value() == 1:
        led.value(True)
        led2.value(False)
    else:
        led.value(False)
        led2.value(True)
    sleep(0.1)