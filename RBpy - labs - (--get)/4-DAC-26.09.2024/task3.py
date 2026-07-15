import RPi.GPIO as GPIO
maxmV=3.22
pwmout1=21
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmout1,GPIO.OUT)
pwmctrl1=GPIO.PWM(pwmout1,0.001)
try:
    inp=int(input())
    while 0<=inp<=100:
        print(f'{round(maxmV/100*inp,3)}mV')
        pwmctrl1.stop()
        pwmctrl1.start(inp)
        inp=int(input())
   
finally:
    print("Argument exeption invoked. Ending.")
    pwmctrl1.stop()
    GPIO.output(pwmout1,0)
    GPIO.cleanup()