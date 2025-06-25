from audio_notification import Audio_Notification
from time import sleep

audio = Audio_Notification

print("Testing Audio Notification")
sleep(3)
audio.beep(self, 1000, 500)
print("Beep() passed")
sleep(1)
audio.warning_on(self)
print("Warning_on() passed")
sleep(1)
audio.warning_off(self)
print("Warning_off() passed")
sleep(1)
print("Audio Notification Test Complete")