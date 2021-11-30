from strategies import *
from functions import *

####################################################################################################################

# set trading variables
PERCENTAGE_OP = 0.1
PERCENTAGE_TP = 1
PERCENTAGE_SL = 3
MARTINGALE_MAX = 0
MARTINGALE_SWITCHING = True
MARTINGALE_VALUE = 2.25

####################################################################################################################

# get current balance
balance = get_balance()

print("\n============================================\n")
print("BINOBOT is Starting...")
print("By: Christensen Mario Frans")
print(f"\n{'STARTING BALANCE:':20}", 'Rp. 'f'{balance:,}')
print("\n============================================\n")

# set target balance using current balance
balance_tp = int(balance + balance * (PERCENTAGE_TP/100))
balance_sl = int(balance - balance * (PERCENTAGE_SL/100))

# set open position amount
op = int(balance * (PERCENTAGE_OP/100))
if op<14000: op = 14000

# list to store open position & martingale values
op_list = [op]

# calculate martingale up to level 9
if MARTINGALE_VALUE==0: 
    for i in range(9): op_list.append( int(sum(op_list) * 100/80) )
else:
    for i in range(9): op_list.append( int(op_list[i]*MARTINGALE_VALUE) )

####################################################################################################################

# golden_moment_strategy(balance, balance_tp, balance_sl, op_list, MARTINGALE_MAX, MARTINGALE_SWITCHING)
# random_strategy(balance, balance_tp, balance_sl, op_list, MARTINGALE_MAX, MARTINGALE_SWITCHING)

####################################################################################################################
 
