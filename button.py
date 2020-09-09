import RPi.GPIO as GPIO
import time
import threading
from pygame import mixer

mixer.init()
GPIO.setmode(GPIO.BCM)
INPUT = 24
GPIO.setwarnings(False)
GPIO.setup([INPUT], GPIO.IN , pull_up_down=GPIO.PUD_DOWN)
isFirstPress = True
def music_thread():
    mixer.music.load('./audio/Moose-Sound.wav')
    mixer.music.play()

def handle(pin):
    global isFirstPress
    if isFirstPress == True:
        t = threading.Thread(target=music_thread)
        t.daemon = True
        t.start()
        print("starting playback")
        isFirstPress = False
        time.sleep(3)
    else:
        isFirstPress = True

GPIO.add_event_detect(INPUT, GPIO.RISING, handle)

while True:
    time.sleep(1e6)