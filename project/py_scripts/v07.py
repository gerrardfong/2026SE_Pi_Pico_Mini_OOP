from controller import PedestrianSubSystem, TrafficLightSubsystem
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from led_light import Led_Light
from time import sleep

pedestrian_red = Led_Light(17, True, True)
pedestrian_green = Led_Light(19, False, True)
traffic_green = Led_Light(6, False, True)
traffic_amber = Led_Light(5, False, True)
traffic_red = Led_Light(3, False, True)
pedestrian_button= Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

light = TrafficLightSubsystem(traffic_red, traffic_amber, traffic_green, False)

def PedestrianSubsystem_driver():
    pedestrian = PedestrianSubSystem()
    pedestrian.show_stop() 
    print("Pedestrian Light is off")
    sleep(3)
    pedestrian.show_walk()

def Traffic_Subsystem_Driver():
    print("Testing Traffic Light in 5 seconds")
    sleep(5)
    light.show_red()
    print("Pass if: Red OFF, Amber OFF, Green ON")
    sleep(10)
    light.show_green()
    print("Pass if: ")
    sleep(10)
    light.show_amber()
    print("Pass if: Red OFF, Amber ON, Green OFF")
    sleep(10)
    print("Traffic Light Subsystem Test Complete")

Traffic_Subsystem_Driver()