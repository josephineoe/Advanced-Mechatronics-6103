from datetime import datetime
from time import sleep
import random

log = open("log.txt", "w")

for i in range(60):
    now = str(datetime.now())
    # Generate some random data in the range 0-1024
    sensor1 = random.randint(0, 25)
    sensor2 = random.uniform(0, 5.00)
    log.write(now + " " + str(sensor1) + "\n")
    print(now + " sensor1:  " + str(sensor1) + "\n")
    log.write(now + " " + str(sensor2) + "\n")
    print(now + " sensor2:  " + str(sensor2) + "\n")
    log.flush()
    sleep(1)
log.close()