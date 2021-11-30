import pyautogui
from functions import read_screenshot
from variables import *

####################################################################################################################

""" FIND REGION (TRIAL & ERROR) """

# set region
# REGION = (2030, 230, 330, 100)

# screenshot region
# image = pyautogui.screenshot(region=REGION)
# image.save(PATH_TEST)

####################################################################################################################

""" TEST SAVED REGIONS (SCREENSHOT & READ TEXTS) """

# regions = [SS_RSI, SS_STOCHASTIC, SS_PRICE, SS_EARNINGS]
# paths = [PATH_RSI, PATH_STOCHASTIC, PATH_PRICE, PATH_EARNINGS]
# names = ['RSI:', 'Stochastic:', 'Price:', 'Earnings:']

# regions = [SS_RSI, SS_STOCHASTIC, SS_EARNINGS]
# paths = [PATH_RSI, PATH_STOCHASTIC, PATH_EARNINGS]
# names = ['RSI:', 'Stochastic:', 'Earnings:']

# capture screenshots
# for region in regions:
#     image = pyautogui.screenshot(region=region)
#     image.save(paths[ regions.index(region) ])

# read screenshots captured
# for path in paths:
#     print( names[ paths.index(path) ], read_screenshot(path) )

####################################################################################################################

