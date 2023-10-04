import RPi.GPIO as rp
import time as t

leds = [9,10,22,27,17,4,3,2]
dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

rp.setmode(rp.BCM)

rp.setup(dac, rp.OUT)
rp.setup(leds, rp.OUT)
rp.setup(troyka, rp.OUT, initial=rp.HIGH)
rp.setup(comp, rp.IN)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def adc():
    numd = 0
    for i in range(7,-1,-1):
        numd += 2**i
        rp.output(dac,decimal2binary(numd))
        t.sleep(0.05)
        if rp.input(comp) == 1:
            numd -= 2**i
    return numd

def adc1():
    for i in range(256):
        num_dac = decimal2binary(i)
        rp.output(dac,num_dac)
        t.sleep(0.008)
        if rp.input(comp) == 1:
            break
    return i

def led(n):
    col = int(n / 256 * 9)
    led_znac = [0]*8
    for i in range(col):
        led_znac[i] = 1
    return led_znac
    

try:
    while True:
        v = adc1()
        rp.output(leds,led(v))
        
finally:
    rp.output(13,0)
    rp.output(dac,0)
    rp.cleanup()

