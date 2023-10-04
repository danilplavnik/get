import RPi.GPIO as rp
import time as t


dac = [8,11,7,1,0,5,12,6]
comp = 14
troyka = 13

rp.setmode(rp.BCM)

rp.setup(dac, rp.OUT)
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

try:
    while True:
        v = adc()
        print(v, '{:.2f}v'.format(3.3 * v / 256))
finally:
    rp.output(13,0)
    rp.output(dac,0)
    rp.cleanup()

