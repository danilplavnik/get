import RPi.GPIO as rp # импортируем библиотеку работы с платой
import time # импортируем библиотеку работы с временем
import matplotlib.pyplot as plt # импортируем библиотеку построения графиков

leds = [2,3,4,17,27,22,10,9] # список пинов светодиодов
dac = [8,11,7,1,0,5,12,6] # список пинов светодиодов ЦАП
comp = 14 # пин компоратора
troyka = 13 # пин troyka модуля

rp.setmode(rp.BCM) # настраеваем режим обращения к пинам

rp.setup(dac, rp.OUT) # настраеваем пины для управления ЦАП
rp.setup(leds, rp.OUT) # настраеваем пины для управления светодиодами
rp.setup(troyka, rp.OUT) # настраеваем пин для управления напряжением на входе тройка-модуля
rp.setup(comp, rp.IN) # настраеваем пин для чтения значения на выходе компаратора

# Функция превода 10-го числа до 2-го числа
def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

# Функция измеряющая напряжение на выходе тройка-модуля
def adc():
    numd = 0
    for i in range(7,-1,-1):
        numd += 2**i
        rp.output(dac,decimal2binary(numd))
        time.sleep(0.008)
        if rp.input(comp) == 1:
            numd -= 2**i
    return numd

# Функция выводящая двоичное представление числа в область светодиодов
def leds_show_bin(dec):
    rp.output(leds,decimal2binary(dec))


data_mesure = [] # список значений измеренного напряжения
begin_exp = 0 # время начала эксперемента
end_exp = 0 # время конца эксперемента
deltat = 0 # общая продолжительность эксперимента

try:
    begin_exp = time.time() # сохраняем в переменную момент начала измерений
    rp.output(troyka, 1) # подаем напряжение 3.3В на вход тройка-модуля
    print('Зарядка конденсатора')
    volttroyka = 3.3 * adc() / 256 # измеряем напряжение на выходе тройка-модуля
    while volttroyka <= 2.655:
        data_mesure.append(volttroyka) # добавляем новые измерения в список
        volttroyka = 3.3 * adc() / 256 # измеряем напряжение на выходе тройка-модуля
        leds_show_bin(adc()) # выводим представление в область LED
        print(volttroyka) # выводим напряжение на выходе тройка-модуля в терминал

    rp.output(troyka, 0) # подаем напряжение 0.0В на вход тройка-модуля
    print('Разрядка конденсатора')
    volttroyka = 3.3 * adc() / 256 # измеряем напряжение на выходе тройка-модуля
    while volttroyka >= 2.1657:
        data_mesure.append(volttroyka) # добавляем новые измерения в список
        volttroyka = 3.3 * adc() / 256 # измеряем напряжение на выходе тройка-модуля
        leds_show_bin(adc()) # выводим представление в область LED
        print(volttroyka) # выводим напряжение на выходе тройка-модуля в терминал

    end_exp = time.time() # сохраняем в переменную момент конца измерений
    deltat = end_exp - begin_exp # определяем продолжительность эксперимента

    print('Общая продолжительность:', deltat, 'с')
    print('Период одного измерения:', deltat/len(data_mesure), 'с')
    print('Средняя частота дискретизации:', (len(data_mesure)/deltat), 'Гц')
    print('Шаг квантования АЦП: 0.0129 В')
    print('Средняя частота дискретизации:', (len(data_mesure)/deltat), 'Гц')


    plt.plot(data_mesure) # строим график

    print('Записываем в файл')
    with open("data.txt", "w") as outfile:
        outfile.write("\n".join([str(item) for item in data_mesure]))

    with open("settings.txt", "w") as outfile:
        outfile.write("\n".join(['Шаг квантования АЦП: 0.0129 В', f'Средняя частота дискретизации: {len(data_mesure/deltat)} Гц']))

finally:
    rp.output(leds,0)
    rp.output(dac,0)
    rp.cleanup()
    plt.show()