import RPi.GPIO as rp
import time as t
rp.setmode(rp.BCM)
rp.setup(24, rp.OUT)
p = rp.PWM(24,1000)
d = 0
try:
    while True:
        d  = int(input())
        print()
        p.start(d)
        input('Press return to stop:')
        p.stop()
finally:
    rp.output(24,0)
    rp.cleanup()

