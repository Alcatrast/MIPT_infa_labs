import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
troyka = 13
comp = 14


def dec2bin(d):
	number = bin(d)[2:].zfill(8)
	number = list(map(int, number))
	return number

def adc():
    for i in range (0, 256):
        GPIO.output(dac, dec2bin(i))
        time.sleep(0.01)
        c = GPIO.input(comp)
        if c == 1:
            return i
                    
    return 255

def adc_opti():
    number = [1, 1, 1, 1, 1, 1, 1, 1]
    GPIO.output(dac, number)
    time.sleep(0.005)
    c = GPIO.input(comp)
    if c == 0:
        return 255
    for i in range(0, 8):
        number[i] = 0
        GPIO.output(dac, number)
        time.sleep(0.005)
        c = GPIO.input(comp)
        if c == 0:
            number[i] = 1
    return int(''.join(str(x) for x in number), 2)
        

try:
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(dac + leds, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(comp, GPIO.IN)
    
    
    time_start = time.time_ns()
    
    charging_v = []
    discharging_v = []
    
    while True:
        #Подготовка
        print("Разряди кондёр")
        time.sleep(5)
        
        # Зарядка
        print("Началась зарядка")
        v255 = adc_opti()
        v = v255 / 255 * 3.3
        t = time.time_ns() - time_start
        GPIO.output(troyka, GPIO.HIGH)
        while (v255 < 210):
            print(v255)
            charging_v.append((t, v))
            v255 = adc_opti()
            v = v255 / 255 * 3.3
            t = time.time_ns() - time_start
        for i in range(0, len(charging_v), int(len(charging_v) / 5)):
            print(f"{charging_v[i][0]} нс {charging_v[i][1]} В")
            
        with open("charge.txt", "w") as f:
            for i in range(0, len(charging_v)):
                f.write(f"{charging_v[i][0]} {charging_v[i][1]}\n")
        plt.plot(charging_v)
        plt.show()
        
        # Разрядка
        print("Началась разрядка")
        v255 = adc_opti()
        v = v255 / 255 * 3.3
        t = time.time_ns() - time_start
        GPIO.output(troyka, GPIO.LOW)
        while (v255 > 50):
            print(v255)
            discharging_v.append((t, v))
            v255 = adc_opti()
            v = v255 / 255 * 3.3
            t = time.time_ns() - time_start
        for i in range(0, len(discharging_v), int(len(discharging_v) / 5)):
            print(f"{discharging_v[i][0]} нс {discharging_v[i][1]} В")
            
        with open("discharge.txt", "w") as f:
            for i in range(0, len(discharging_v)):
                f.write(f"{discharging_v[i][0]} {discharging_v[i][1]}\n")
        
        
                


        t = []
        v = []

        with open("charge.txt", "r") as f:
            a = f.readlines()
            for i in a:
                i = i.split()
                t.append(int(i[0]))
                v.append(float(i[1]))
            
        plt.plot(t, v)
        plt.show()

        t = []
        v = []

        with open("discharge.txt", "r") as f:
            a = f.readlines()
            for i in a:
                i = i.split()
                t.append(int(i[0]))
                v.append(float(i[1]))
            
        plt.plot(t, v)
        plt.show()

        exit()
        time.sleep(0.01)
    
    
	
finally:
	print("Выход...")
	GPIO.output(dac, GPIO.LOW)
	GPIO.cleanup()

