import RPi.GPIO as rp
import time as t
dac = [8,11,7,1,0,5,12,6]
rp.setmode(rp.BCM)
rp.setup(dac, rp.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
T = float(input())/512
try:
    g = 0
    i  = 1
    while True:
        if g == 0:
            i = 1
        elif g == 255:
            i = -1
        j = decimal2binary(g)
        rp.output(dac,j)
        t.sleep(T)
        g += i
finally:
    rp.output(dac,0)
    rp.cleanup()
