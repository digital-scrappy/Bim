import RPi.GPIO as GPIO
import time
import os, sys
import requests
import json
import datetime
pin_mapping = {
    'a' : 3,
    'b' : 5,
    'c' : 7,
    'd' : 8,
    'e' : 11,
    'f' : 13,
    'g' : 15,
    }

class SevenSegmentDisplay:

    def __init__(self, pin_mapping, GPIO_mode = GPIO.BOARD, GPIO_warning= True, common = "anode"):

        self.symbol_dict= {
            "0" : ["a", "b", "c", "e", "f", "g"],
            "1" : ["a", "g"],
            "2" : ["a", "b", "d", "e", "f"],
            "3" : ["a", "b", "d", "f", "g"],
            "4" : ["a", "c", "d", "g"],
            "5" : ["b", "c", "d", "f", "g"],
            "6" : ["c", "b", "d", "e", "f", "g"],
            "7" : ["a", "b", "g"],
            "8" : ["a", "b", "c", "d", "e", "f", "g"],
            "9" : ["a", "b", "c", "d", "f", "g"]
        }


        self.pin_mapping = pin_mapping
        self.all_pins = pin_mapping.values()
        print(self.all_pins)
        self.common = common
        self.GPIO_mode = GPIO_mode
        self.GPIO_warning = GPIO_warning

    def setup(self):
        GPIO.setwarnings(self.GPIO_warning)
        GPIO.setmode(self.GPIO_mode)

        for pin in self.all_pins:
            GPIO.setup(pin, GPIO.OUT)




    def disable(sel):
        GPIO.cleanup()

    def clear(self):
        for i in self.all_pins:
            if self.common == "anode":
                GPIO.output(i, 1)
            elif self.common == "cathode":
                GPIO.output(i, 0)

    def enable_pins(self, pins):
        for i in pins:
            if self.common == "anode":
                GPIO.output(i, 0)
            elif self.common == "cathode":
                GPIO.output(i, 1)





    def display(self, symbol):
        to_update = [ self.pin_mapping[pin] for pin in self.symbol_dict[symbol]]

        self.clear()
        self.enable_pins(to_update)



disp = SevenSegmentDisplay(pin_mapping)
disp.setup()

failed = 0
print(datetime.datetime.now())
while True:


    r = requests.get('https://apps.static-access.net/ViennaTransport/monitor/?line=42&station=Sommarugagasse&towards=Schottentor&countdown')
    response = r.json()


    try:
        countdown = response[0]['countdown'][0]
        if countdown == 0:
            countdown = response[0]['countdown'][1]
        disp.display(str(countdown))

    except:
        failed += 1
        print(datetime.datetime.now())
        print("failed to fetch new countdown")
        print(f"failed request {failed}")

        if failed == 2:
            countdown -= 1
            failed = 0

    else:
        failed = 0
    time.sleep(30)
