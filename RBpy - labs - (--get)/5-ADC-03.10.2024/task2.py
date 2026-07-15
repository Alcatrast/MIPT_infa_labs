import RPi.GPIO as gp
import time
dac = [8,11,7,1,0,5,12,6]
comp=14
troyka=13
gp.setmode(gp.BCM)
gp.setup(dac,gp.OUT)
gp.setup(troyka,gp.OUT, initial=gp.HIGH)
gp.setup(comp,gp.IN)

def tobinlist(x):
    res=list(map(int,bin(x)[2:]))
    return ([0]*(8-len(res)))+res
def bindec(x):
    res=0
    for i in x:
        res*=2
        res+=i
    return res

def adc():
    d=[0]*8
    for i in range(0,8):
        d[i]=1
        gp.output(dac,d)
        time.sleep(0.1)
        c=gp.input(comp)
        if c ==1:
            d[i]=0
    return d
try:
    while True:
        hih=adc()
        gp.output(dac,hih)
        hah=bindec(hih)
        print(hah,round(3.3*hah/256,3))
finally:
    gp.output([troyka]+dac,0)
    gp.cleanup()