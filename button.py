import RPi.GPIO as GPIO
import time
from pygame import mixer

mixer.init()
GPIO.setmode(GPIO.BCM)
INPUT_PIN = 23
GPIO.setwarnings(False)
GPIO.setup(INPUT_PIN, GPIO.IN , pull_up_down=GPIO.PUD_DOWN)
isFirstPress = True

def music():
    mixer.music.load('./audio/Moose-Sound.mp3')
    mixer.music.play()

def handle(pin):
    global isFirstPress
    if isFirstPress == True:
        print("starting playback")
        music()
        isFirstPress = False
        time.sleep(3)
        isFirstPress = True
    else:
        return

GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, callback=handle)

while True:
    time.sleep(1e6)