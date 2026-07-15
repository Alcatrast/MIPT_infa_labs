import RPi.GPIO as GPIO
delay= 1
ledouts=[2,3,4,17,27,22,10,9]
auxins =[21,20,26,16,19,25,23,24]
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
for i in ledouts:
    GPIO.setup(i,GPIO.OUT)
for i in auxins:
    GPIO.setup(i,GPIO.IN)

while True:
    for i in range(len(auxins)):
        GPIO.output(ledouts[i], (GPIO.input(auxins[i])))