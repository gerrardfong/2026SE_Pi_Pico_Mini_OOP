from led_light import Led_Light
from time import sleep, time

self = Led_Light(3)

def unit_test_on_off(self):
    # Turn on the light
    self.high()
    if self.value() == 1:
        # After turning on the light print statement
        print("LED is on. ")
        sleep(1)
    elif self.high() == True:
        # Check if light is on 
        self.low()
        # Print Exception Statement 
        print("LED is off")
        sleep(1)
        print("Unit Test succesfull for on() and off() functions")
    else:
        print("Something went wrong.")

def unit_test_toggle(self):
    self.toggle()
    # Turn on LED
    if self.value == 1:
        #Exception Statement 
        print("Succesfully toggled on")
        sleep(1)
    elif self.value == 0:
        #Exception Statement
        print("Successfully toggled off")

unit_test_toggle(self)
