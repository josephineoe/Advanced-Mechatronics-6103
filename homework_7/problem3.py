import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

red = 17 #pin 11
yellow = 27 #pin 13
green = 22 #pin 15

GPIO.setup(red,GPIO.OUT)
GPIO.setup(yellow,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

while True:
    GPIO.output(red,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(red,GPIO.LOW)
    GPIO.output(yellow,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(yellow,GPIO.LOW)
    GPIO.output(green,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(green,GPIO.LOW)