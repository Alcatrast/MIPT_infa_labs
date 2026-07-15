import RPi.GPIO as GPIO
import time
delay= 1
datouts=[8,11,7,1,0,5,12,6]
number =[0,1,0,0,1,1,0,1]
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
for i in datouts:
    GPIO.setup(i,GPIO.OUT)

def clear():
     for i in datouts:
        GPIO.output(i,0)

def write():
    for i in range(len(number)):
        GPIO.output(datouts[i],number[i])

number =[0,0,0,0,0,0,0,0]
clear()
write()
time.sleep(15)
clear()
GPIO.cleanup()