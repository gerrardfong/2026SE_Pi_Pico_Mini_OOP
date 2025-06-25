from led_light import Led_Light
from time import sleep, time


self = Led_Light(3)

def unit_test_on_off():
    # Turn on the light
    self.on()
    if self.value() == 1:
        # After turning on the light print statement
        print("LED is on. ")
        sleep(1)
    elif self.on() == True:
        # Check if light is on 
        self.off()
        # Print Exception Statement 
        print("LED is off")
        sleep(1)
        print("Unit Test succesfull for on() and off() functions")
    else:
        print("Something went wrong.")

def unit_test_toggle():
    self.toggle()
    # Turn on LED
    if self.value == 1:
        #Exception Statement 
        print("Succesfully toggled on")
        sleep(1)
    elif self.value == 0:
        #Exception Statement
        print("Successfully toggled off")

def unit_test_flash():
    self.flash()
    #Flash LED
    print("LED flashing")
    sleep(1)


def unit_test():
    unit_test_on_off()
    sleep(1)
    unit_test_toggle()
    sleep(1)
    unit_test_flash()
    print("Unit Test completed")

unit_test()
