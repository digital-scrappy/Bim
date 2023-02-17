#              .';:cc;.
#            .,',;lol::c.
#            ;';lddddlclo
#            lcloxxoddodxdool:,.
#            cxdddxdodxdkOkkkkkkkd:.
#          .ldxkkOOOOkkOO000Okkxkkkkx:.
#        .lddxkkOkOOO0OOO0000Okxxxxkkkk:
#       'ooddkkkxxkO0000KK00Okxdoodxkkkko
#      .ooodxkkxxxOO000kkkO0KOxolooxkkxxkl
#      lolodxkkxxkOx,.      .lkdolodkkxxxO.
#      doloodxkkkOk           ....   .,cxO;
#      ddoodddxkkkk:         ,oxxxkOdc'..o'
#      :kdddxxxxd,  ,lolccldxxxkkOOOkkkko,
#       lOkxkkk;  :xkkkkkkkkOOO000OOkkOOk.
#        ;00Ok' 'O000OO0000000000OOOO0Od.
#         .l0l.;OOO000000OOOOOO000000x,
#            .'OKKKK00000000000000kc.
#               .:ox0KKKKKKK0kdc,.
#                      ...
#
# Author: peppe8o
# Blog: https://peppe8o.com
# Date: Nov 8th, 2020
# Version: 1.0

import RPi.GPIO as GPIO
import sys
from display import get_display_pinlist

#define PINs according to cabling
dataPIN = 17
latchPIN = 27
clockPIN = 22

#set pins to putput
GPIO.setmode(GPIO.BCM)
GPIO.setup((dataPIN,latchPIN,clockPIN),GPIO.OUT)

#define shift register update function
def shift_update(input,data,clock,latch):
  #put latch down to start data sending
  GPIO.output(clock,0)
  GPIO.output(latch,0)
  GPIO.output(clock,1)
  
  #load data in reverse order
  for i in range(7, -1, -1):
    GPIO.output(clock,0)
    GPIO.output(data, int(input[i]))
    print(int(input[i]))
    GPIO.output(clock,1)
  
  #put latch up to store data on register
  GPIO.output(clock,0)
  GPIO.output(latch,1)
  GPIO.output(clock,1)

def bools_to_str(bools):
    out = ""
    for b in bools:
        out += "1" if b else "0"

    return out

while True:

    symbol = input("int pls:")
    if symbol == "exit":
        break

    pin_list = get_display_pinlist(symbol)
    print(pin_list)
    # shift_register.set_by_list(pin_list)
    shift_update(bools_to_str(pin_list),dataPIN,clockPIN,latchPIN)

#main program, calling shift register function
#uses "sys.argv" to pass arguments from command line

#PINs final cleaning

GPIO.cleanup()
