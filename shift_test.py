from pi74HC595 import pi74HC595
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
shift_register = pi74HC595(DS =11, ST = 13, SH=15)

shift_register.set_by_list([1, 1, 1, 1, 1, 1, 1, 1])
