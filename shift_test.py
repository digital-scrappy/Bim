from pi74HC595 import pi74HC595
import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595(DS =11, ST = 13, SH=15)

while True:
    shift_register.set_by_list([1, 1, 1, 1, 1, 1, 1, 1])
    sleep(1)
    shift_register.set_by_list([0, 0, 0, 0, 0, 0, 0, 0])
    sleep(1)
