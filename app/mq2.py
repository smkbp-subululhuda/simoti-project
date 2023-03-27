from time import sleep
import time
import sys
import RPi.GPIO as GPIO
from datetime import datetime

now = datetime.now()
sekarang = now.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def action(pin):
    print(sekarang, 'Asap Terdeteksi!')
    #fire()
    
GPIO.add_event_detect(23, GPIO.RISING)
GPIO.add_event_callback(23, action)

try:
    print('mendeteksi asap')
    while True:
        time.sleep()
except KeyboardInterrupt:
     GPIO.cleanup()
     sys.exit()
