import RPi.GPIO as GPIO
import time
delay= 1
ledouts=[2,3,4,17,27,22,10,9]
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

for i in ledouts:
    GPIO.setup(i,GPIO.OUT)

while True:
    for i in ledouts:
        GPIO.output(i,1)
        time.sleep(delay)
        GPIO.output(i,0)

