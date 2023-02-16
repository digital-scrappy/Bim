from typing import List

# def get_display_pinlist(symbol :str, point :bool = False) -> List[bool]:
def get_display_pinlist(symbol :str) -> List[bool]:

    pin_dict = {
        "0top": "mid",
        "1top": "lefttop",
        "2top": None,
        "3top": "top",
        "4top": "righttop",
        "0bot": None,  # no clue
        "1bot": "leftbot",
        "2bot": "bot",
        "3bot": "rightbot",
        "4bot": None,  # power in
        }

    segment_indices = {
        "mid"      : 0,
        "lefttop"  : 1,
        # "point"    : 2,
        "top"      : 3,
        "righttop" : 4,
        "leftbot"  : 5,
        "bot"      : 6,
        "rightbot" : 7,
        }
    symbol_dict = {
        "0": ["righttop", "top", "lefttop", "leftbot", "bot", "rightbot"],
        "1": ["righttop", "rightbot"],
        "2": ["righttop", "top", "mid", "leftbot", "bot"],
        "3": ["righttop", "top", "mid", "bot", "rightbot"],
        "4": ["righttop", "lefttop", "mid", "rightbot"],
        "5": ["top", "lefttop", "mid", "bot", "rightbot"],
        "6": ["lefttop", "top", "mid", "leftbot", "bot", "rightbot"],
        "7": ["righttop", "top", "rightbot"],
        "8": ["righttop", "top", "lefttop", "mid", "leftbot", "bot", "rightbot"],
        "9": ["righttop", "top", "lefttop", "mid", "bot", "rightbot"],
    }
    on_names = symbol_dict[symbol]
    out_bools = [False if key in on_names else True for key in segment_indices.keys()]


    return out_bools
         
        
            

        
        

# class SevenSegmentDisplay:
#     """
#     class for my wierd common annode seven segment displays

#     """

#     def __init__(self, pin_numbers):
#         ''' pin numbers should be provided in the following order 
#         ["0top", "1top", "2top", "3top", "4top", "1bot", "2bot", "3bot"]
#         '''
#         #just for reference


#         #just for reference
#         self.rev_pin_dict = {
#             "mid"      : "0top",
#             "lefttop"  : "1top",
#             "point"    : "2top",
#             "top"      : "3top",
#             "righttop" : "4top",
#             "leftbot"  : "1bot",
#             "bot"      : "2bot",
#             "rightbot" : "3bot",
#         }


#         self.segment_indices = {
#             "mid"      : 0,
#             "lefttop"  : 1,
#             "point"    : 2,
#             "top"      : 3,
#             "righttop" : 4,
#             "leftbot"  : 5,
#             "bot"      : 6,
#             "rightbot" : 7,
#         }

#         self.symbol_dict = {
#             "0": ["righttop", "top", "lefttop", "leftbot", "bot", "rightbot"],
#             "1": ["righttop", "rightbot"],
#             "2": ["righttop", "top", "mid", "leftbot", "bot"],
#             "3": ["righttop", "top", "mid", "bot", "rightbot"],
#             "4": ["righttop", "lefttop", "mid", "rightbot"],
#             "5": ["top", "lefttop", "mid", "bot", "rightbot"],
#             "6": ["lefttop", "top", "mid", "leftbot", "bot", "rightbot"],
#             "7": ["righttop", "top", "rightbot"],
#             "8": ["righttop", "top", "lefttop", "mid", "leftbot", "bot", "rightbot"],
#             "9": ["righttop", "top", "lefttop", "mid", "bot", "rightbot"],
#         }
        

#     def setup(self):

#     def disable(self):


#     def clear(self):
#         for i in self.all_pins:
#             if self.common == "anode":
#                 GPIO.output(i, 1)
#             elif self.common == "cathode":
#                 GPIO.output(i, 0)

#     def enable_pins(self, pins):
#         for i in pins:
#             if self.common == "anode":
#                 GPIO.output(i, 0)
#             elif self.common == "cathode":
#                 GPIO.output(i, 1)

#     def display(self, symbol):
#         to_update = [self.pin_mapping[pin] for pin in self.symbol_dict[symbol]]

#         self.clear()
#         self.enable_pins(to_update)
