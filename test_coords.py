import time, random
from pynput.mouse import Controller
from functions import open_position, get_balance
from variables import *

mouse = Controller()

####################################################################################################################

""" FIND COORDINATE """

# wait for 3 seconds for user to place pointer on desired location
# time.sleep(3)
# print("Pointer's Coordinates Are:", mouse.position)

# test pointer coordinates
# POSITION = (543, 88)
# mouse.position = POSITION

####################################################################################################################

""" TEST SAVED COORDINATES """

# coordinates = [BALANCE, INPUT, BUY, SELL, BLANK, REFRESH]

# test pointer to each coordinate
# for coordinate in coordinates:
#     time.sleep(2)
#     mouse.position = coordinate

# test pointer functions
# amount = random.randint(14000, 35000)
# open_position(amount, SELL, 0)
# open_position(amount, BUY, 0)
# get_balance()

####################################################################################################################
