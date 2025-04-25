import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 1 #pin 12
B1 = 0 #pin 11
B2 = 2 #pin 13

GPIO.setup(B1,GPIO.IN)
GPIO.setup(B2,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

pi_pwm = GPIO.PWM(led, 1000)
pi_pwm.start(0)

while True:
    inputValue=GPIO.input(B1)
    inputValue=GPIO.input(B2)

    if(inputValue == False): #active low button gives 0 when pressed
        for duty in range(0, 101, 1):
            pi_pwm.ChangeDutyCycle(duty)
            sleep(0.5)

    for duty in range(100, -1. -1):    
        if(inputValue == False): #active low button gives 0 when pressed
            pi_pwm.ChangeDutyCycle(duty)
            time.sleep(0.5)
        else:
            print("Press button")
    time.sleep(1)