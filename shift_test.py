from pi74HC595 import pi74HC595
import RPI.GPIO as gpio

gpio.setmode(gpio.Board)
shift_register = pi74HC595(DS =11, ST = 13, SH=15)
