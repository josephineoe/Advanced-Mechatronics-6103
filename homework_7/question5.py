from datetime import datetime
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
Ping_pin = 23
LED_pin = 22

#Open file to write and save distance data
file = open("rdistancelogs.txt", "w")
#While loop to monitor distance
while(1):
    GPIO.setup(Ping_pin, GPIO.OUT)
    GPIO.setup(LED_pin, GPIO.OUT)
    #First set Ping_pin to output to send signal

    #cleanup output to send a clean high signal
    GPIO.output(Ping_pin, 0)
    time.sleep(0.000002)
    #send signal, 5us signal to cause Ping))) to emit chirp
    GPIO.output(Ping_pin, 1)
    time.sleep(0.000005)
    #cleanup output pin
    GPIO.output(Ping_pin, 0)
    #Make Ping_pin input pin to monitor Ping sensor SIG pin
    GPIO.setup(Ping_pin, GPIO.IN)
    # starttime=time.time()
    while GPIO.input(Ping_pin)==0:
        starttime=time.time()
    while GPIO.input(Ping_pin)==1:
        endtime=time.time()
         #Duration that the high pulse lasts 
    duration=endtime-starttime
    #Round trip distance from Ping2Object and Object2Ping
    distance=duration*34000
    #Ping2Object distance
    distance=distance/2
    print(distance)
    time.sleep(2)
    file.write(str(distance)+"\n")
file.close()

while True: 
    if distance >= 20:
        GPIO.output(LED_pin, 1)
        time.sleep(0.5)
    else:
        GPIO.output(LED_pin, 0)

