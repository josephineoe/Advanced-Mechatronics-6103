import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 18  #12 
B1 = 27   #13
B2 = 22   #15 


GPIO.setup(B1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(B2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)


pi_pwm = GPIO.PWM(led, 1000)
pi_pwm.start(0)

brightness = 0 

while True:
    if GPIO.input(B1) == False:  #button set to active low so when pressed sends 0
        if brightness < 100:
            brightness += 10
            pi_pwm.ChangeDutyCycle(brightness)
        time.sleep(0.2)  # debounce delay

    elif GPIO.input(B2) == False:
        if brightness > 0:
            brightness -= 10
            pi_pwm.ChangeDutyCycle(brightness)
        time.sleep(0.2) 

    else:
        time.sleep(0.05)
