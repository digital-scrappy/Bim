from pi74HC595 import pi74HC595
from display import get_display_pinlist


import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595(DS =11, ST = 13, SH=15)

while True:

    symbol = input("int pls:")

    pin_list = get_display_pinlist(symbol)
    print(pin_list)
    shift_register.set_by_list(pin_list)
