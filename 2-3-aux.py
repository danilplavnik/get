import RPi.GPIO as rp
import time as t
leds = [2,3,4,17,27,22,10,9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
rp.setmode(rp.BCM)
rp.setup(leds, rp.OUT)
rp.setup(aux, rp.IN)
rp.output(leds,1)
while True:
    for i in range(8):
        rp.output(leds[i],rp.input(aux[i]))
rp.output(leds,0)
rp.cleanup()