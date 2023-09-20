import RPi.GPIO as rp
from matplotlib import pyplot as plt
dac = [8,11,7,1,0,5,12,6]
number = [1,1,1,0,0, 1,1,1]
rp.setmode(rp.BCM)
rp.setup(dac, rp.OUT)
rp.output(dac,number)
rp.output(dac,0)
rp.cleanup()
x = [0, 2, 5, 32, 64, 127, 255]
y = [0.52, 0.077, 0.116, 0.458, 0.867, 1.671, 3.261]
plt.scatter(x,y)
plt.plot(x, y, color ='purple')
plt.show()