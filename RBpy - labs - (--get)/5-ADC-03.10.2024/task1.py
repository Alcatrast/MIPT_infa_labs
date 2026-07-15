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
    for v in range(256):
        s=tobinlist(v)
        gp.output(dac,s)
        time.sleep(0.01)
        if gp.input(comp)==1:
            return v
        return 255
try:
    while True:
        hah=adc()
        print(hah,round(3.3*hah/256,3))
finally:
    gp.output([troyka]+dac,0)