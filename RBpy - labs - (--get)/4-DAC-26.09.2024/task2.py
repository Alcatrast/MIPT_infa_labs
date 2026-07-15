import RPi.GPIO as GPIO
import time
delay= 1
dac=[8,11,7,1,0,5,12,6]
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def bin_list(x):
    res=list(bin(x))[2::]
    return list(map(int,[0]*(8-len(res))+res))
def dac_out(inp):
    for i in range(0,len(dac)):
        outdata=bin_list(inp)
        GPIO.output(dac[i],outdata[i])

try:
    inp=int(input())
    delay=inp/512
    while True:        
        for i in range(0,256):
            dac_out(i)
            time.sleep(delay)
        for i in range(255,-1,-1):
            dac_out(i)
            time.sleep(delay)
finally:
    print("Argument exeption invoked. Ending.")
    GPIO.output(dac,0)
    GPIO.cleanup()