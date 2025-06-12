from machine import Pin
from time import ticks_ms, ticks_diff



class Pedestrian_Button(Pin):
    def __init__(self, pin, debug):
        super().__init__(pin, Pin.IN, Pin.PULL_DOWN)
        self.__debug = debug
        self.__pin = pin
        self.__last_pressed = 0
        self.__pedestrain_waiting = False
        self.button_state
        self.irq(trigger=Pin.IRQ_RISING, handler=self.callback)
        
    def callback(self, pin):
        current_time = ticks_ms()
        if (ticks_diff(current_time, self.__last_pressed) > 200):
            self.__last_pressed = current_time
            self.__pedestrian_waiting = True
            if self.__debug:
                print(f"Button pressed on pin {self.__pin} at {current_time}ms")

    @property
    def button_state(self):
        if self.__debug:
            print(f"Button connected to Pin {self.__pin} is {'WAITING' if self.__pedestrian_waiting else 'NOT WAITING'}")
        return self.__pedestrian_waiting
    
    @button_state.setter
    def button_state(self, value):
        self.__pedestrian_waiting = value
        if self.__debug:
            print(f"Button state on Pin {self.__pin} set to {value}")
    
        
