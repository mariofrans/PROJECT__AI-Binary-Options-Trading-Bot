from functions import *
from variables import *

####################################################################################################################

# 1-MINUTE CHART
def random_strategy(balance, balance_tp, balance_sl, op_list, m_max, m_switching):

    # get data from csv in list for each column
    data = get_csv_data('R', m_max, balance)

    # create lists to store trades' results
    trades_list = []
    martingales_list = []
    
    time_now = datetime.now()

    while True:

        # update time every second
        if (datetime.now() - time_now).seconds == 1 :
            
            time_now = datetime.now()
            print(time_now.strftime("%d/%m/%Y - %H:%M:%S"))

            # wait until time is on the 00th second
            if time_now.strftime("%S")=='00':

                # choose random signal
                signal = random.choice([BUY, SELL])
                print("\n============================================\n")

                if signal==BUY: print('RANDOM CHOICE: BUY\n')
                elif signal==SELL: print('RANDOM CHOICE: SELL\n')

                # trade based on signal
                var_static = [signal, op_list, m_max, m_switching]
                var_return = [balance, trades_list, martingales_list]
                balance, trades_list, martingales_list = trade(var_static, var_return)
    
                # save data to csv file
                set_csv_data(data, balance, trades_list, martingales_list)

                print("\n============================================\n")

            if len(martingales_list)==0: m_largest=0
            else: m_largest=max(martingales_list)

            if balance>=balance_tp or balance<=balance_sl or (m_largest>=m_max and m_max!=0): end_program()
            
            # update current time
            time_now = datetime.now()

####################################################################################################################

# 30-SECOND CHART
def golden_moment_strategy(balance, balance_tp, balance_sl, op_list, m_max, m_switching):

    # get data from csv in list for each column
    data = get_csv_data('GM', m_max, balance)
    
    # create lists to store trades' results
    trades_list = []
    martingales_list = []

    time_now = datetime.now()

    while True:

        # update time every second
        if (datetime.now() - time_now).seconds == 1:

            time_now = datetime.now()
            print(time_now.strftime("%d/%m/%Y - %H:%M:%S"))

            # wait until time is on the 30th second
            if time_now.strftime("%S")=='30':
                
                print("\n============================================\n")

                # read the RSI & STOCHASTIC numbers for the 30th second
                # calculate the time taken to perform these operations
                start_time = time.time()
                rsi_30, stochastic_30 = read_rsi_stochastic()
                end_time = time.time()

                # check if indicators are at OVERBOUGHT or OVERSOLD
                # otherwise, wait for the next 30th second
                if (rsi_30>80 and stochastic_30>80) or (rsi_30<20 and stochastic_30<20):

                    if rsi_30>80 and stochastic_30>80: print('\nOVERBOUGHT: Potential SELL Signal')
                    elif rsi_30<20 and stochastic_30<20: print('\nOVERSOLD: Potential BUY Signal')
                    
                    # wait until 00th second (30s - time taken for it to run prior operations)
                    time.sleep(30 - (end_time - start_time))
                    print(f"\n{'TIME:':10}", datetime.now().strftime("%H:%M:%S"))

                    # read RSI & STOCHASTIC numbers for the 00th second
                    # calculate the time taken to perform these operations
                    start_time = time.time()
                    rsi_00, stochastic_00 = read_rsi_stochastic()
                    end_time = time.time()

                    # check if indicators were previously OVERBOUGHT on the 30th second
                    if rsi_30>80 and stochastic_30>80:

                        # check for SELL signal on the 00th second
                        if rsi_00<80 and rsi_00>50 and stochastic_00<80 and stochastic_00>50:
                            
                            # open SELL position
                            signal = SELL
                            print("\n============================================\n")
                            
                            # trade based on signal
                            var_static = [signal, op_list, m_max, m_switching]
                            var_return = [balance, trades_list, martingales_list]
                            balance, trades_list, martingales_list = trade(var_static, var_return)

                            # save data to csv file
                            set_csv_data(data, balance, trades_list, martingales_list)

                        # indicators fail to indicate SELL signal
                        else: print("\nNevermind...")
                            
                    # check if indicators were previously OVERSOLD on the 30th second
                    elif rsi_30<20 and stochastic_30<20:

                        # check for BUY signal on the 00th second
                        if rsi_00>20 and rsi_00<50 and stochastic_00>20 and stochastic_00<50:
                            
                            # open BUY position
                            signal = BUY
                            print("\n============================================\n")
                            
                            # trade based on signal
                            var_static = [signal, op_list, m_max, m_switching]
                            var_return = [balance, trades_list, martingales_list]
                            balance, trades_list, martingales_list = trade(var_static, var_return)

                            # save data to csv file
                            set_csv_data(data, balance, trades_list, martingales_list)
                            
                        # indicators fail to indicate SELL signal
                        else: print("\nNevermind...")

                print("\n============================================\n")
            
            if len(martingales_list)==0: m_largest=0
            else: m_largest=max(martingales_list)

            if balance>=balance_tp or balance<=balance_sl or (m_largest>=m_max and m_max!=0): end_program()

            # update current time
            time_now = datetime.now()

####################################################################################################################