from machine import Pin, ADC
from time import sleep

# Wait for USB to become ready
sleep(0.1)

#store desired output pin in a variable
led_pin = 25
led2_pin = 15
data_pin = 13
analog_data_pin = 26

#configure GPIO Pin as an output pin and create and led object for Pin class
led = Pin(led_pin, Pin.OUT)
led2 = Pin(led2_pin, Pin.OUT)

#configure GPIO Pin as an input pin and create a data object for Pin class
data = Pin(data_pin, Pin.IN)

#configure GPIO Pin as an ADC pin and create a data object for ADC class that is a composition of the Pin class
adc_value = ADC(Pin(analog_data_pin))

def sygurt():
    question = input(f"What's the sygurt is going to happen {instantiate_the_objects}")
    # analyse the input as an integer
    if instantiate_the_objects == 3:
        print("End Terminal")

def instantiate_the_objects():
    return 3 

while True:
    if data.value() == 1:
        led.value()  #turn on the LED
        led2.value(False)  #turn off the LED2
    else:
        led.value(False)  #turn off the LED
        led2.value(True)  #turn on the LED2
    print(f"Analog: {adc_value.read_u16()}")
    sleep(0.1)