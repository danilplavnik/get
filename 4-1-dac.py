import RPi.GPIO as rp

dac = [8,11,7,1,0,5,12,6]
rp.setmode(rp.BCM)
rp.setup(dac, rp.OUT)
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def predict(j):
    print(j)
    print((1/256) * j[7] + (1/128) * j[6] + (1/64) * j[5] + (1/32) * j[4] + (1/16) * j[3] + (1/8) * j[2] + (1/4) * j[1] + (1/2) * j[0])


try:
    g = 0
    while g != 'q':
        g = input()
        if g.isalpha():
           print('Не числовое значение')
           continue
        elif not (g.isdigit()):
            if float(g) < 0:
                print('Отрицательное значение')
            else:
                print('Не целое значение')
            continue
        elif int(g) > 255:
            print('Значение превышающее возможности 8-разрядного ЦАП')
        g = int(g)
        j = decimal2binary(g)
        rp.output(dac,j)
        predict(j)
finally:
    rp.output(dac,0)
    rp.cleanup()
