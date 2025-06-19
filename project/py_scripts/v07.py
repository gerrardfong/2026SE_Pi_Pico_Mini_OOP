from controller import PedestrianSubSystem, TrafficLightSubsystem
from audio_notification import Audio_Notification
from pedestrian_button import Pedestrian_Button
from led_light from Led_Light
from time import sleep

pedestrian_red = Led_Light(17, True, True)
pedestrian_green = Led_Light(19, False, True)
car_green = Led_Light(6, False, True)
car_amber = Led_Light(5, False, True)
car_red = Led_Light(3, False, True)
pedestrian_button= Pedestrian_Button(22, True)
buzzer = Audio_Notification(27, True)

def PedestrianSubsystem_driver():
    pedestrian = PedestrianSubSystem()
    pedestrian.show_stop()
    print("Pedestrian Light is off")
    sleep(3)
    pedestrian.show_walk()
    

Subsystem_Driver()