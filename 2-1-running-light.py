import RPi.GPIO as rp
import time as t
leds = [2,3,4,17,27,22,10,9]
rp.setmode(rp.BCM)
rp.setup(leds, rp.OUT)
rp.output(leds,1)
rp.output(leds,0)
for j in range(3):
    for i in range(8):
        rp.output(leds[i],1)
        t.sleep(0.2)
        rp.output(leds[i],0)
rp.output(leds,0)
rp.cleanup()