import RPi.GPIO as GPIO
delay= 1
dac=[8,11,7,1,0,5,12,6]
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

def bin_list(x):
    res=list(bin(x))[2::]
    return list(map(int,[0]*(8-len(res))+res))

try:
    inp=int(input())
    while 0<=inp<=255:
        outdata=bin_list(inp)
        print(outdata)
        for i in range(0,len(dac)):
            GPIO.output(dac[i],outdata[i])
        inp=int(input())
finally:
    print("Argument exeption invoked. Ending.")
    GPIO.output(dac,0)
    GPIO.cleanup()