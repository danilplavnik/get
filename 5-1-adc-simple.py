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
    for i in range(256):
        num_dac = decimal2binary(i)
        rp.output(dac,num_dac)
        t.sleep(0.008)
        if rp.input(comp) == 1:
            break
    return i

try:
    while True:
        v = adc()
        print(v, '{:.2f}v'.format(3.3 * v / 256))
finally:
    rp.output(13,0)
    rp.output(dac,0)
    rp.cleanup()

