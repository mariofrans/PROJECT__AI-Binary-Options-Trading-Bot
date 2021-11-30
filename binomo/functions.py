from variables import *

####################################################################################################################

def refresh():

    time.sleep(1)
    pointer_click(REFRESH)
    time.sleep(15)

####################################################################################################################

def pointer_click(coordinates):

    time.sleep(0.1)
    mouse.position = coordinates
    time.sleep(0.1)
    mouse.click(mouse_button.left)
    time.sleep(0.1)

    if coordinates==BUY: 
        print(f"{'CLICK:':10}", "BUY")
        print(f"{'TIME:':10}", datetime.now().strftime("%H:%M:%S"))
    elif coordinates==SELL: 
        print(f"{'CLICK:':10}", "SELL")
        print(f"{'TIME:':10}", datetime.now().strftime("%H:%M:%S"))

####################################################################################################################

def open_position(signal, amount, m_level):

    pointer_click(BLANK)

    mouse.position = INPUT
    time.sleep(0.1)
    mouse.click(mouse_button.left, 2)
    time.sleep(0.1)
    keyboard.type(str(amount))

    if m_level==0: print('\n> OPEN TRADE')
    else: print('\n> MARTINGALE', m_level)
    print(f"{'AMOUNT:':10}", 'Rp. 'f'{amount:,}')
    
    pointer_click(signal)
    pointer_click(BLANK)

####################################################################################################################

def trade(var_static, var_return):

    # calculate the time taken to perform these operations
    start_time = time.time()

    signal, op_list, m_max, m_switching = var_static
    balance, trades_list, martingales_list = var_return

    print('TRADE NUMBER:', len(trades_list)+1)
    print(f'\n-------------------------')

    # open position based on random signal direction
    m_level = 0
    open_position(signal, op_list[m_level], m_level)

    end_time = time.time()

    # wait until RIGHT BEFORE the next minute to determine a martingale or not
    # program waits for (59s - time taken for the program to run prior operations)
    time.sleep(59 - (end_time - start_time))
    print(f"\n{'CHECK:':10}", datetime.now().strftime("%H:%M:%S"))

    # recursive martingale function (up to m_max)
    if m_max>0: m_level = martingale(signal, op_list, m_level, m_max, m_switching)
    martingales_list.append(m_level)

    # make sure that no pop up is blocking
    refresh()

    # update current balance
    balance_before = balance
    balance = get_balance()

    print(f'\n-------------------------')
    print(f"\n{'CURRENT BALANCE:':20}", 'Rp. 'f'{balance:,}')
    print(f"{'PRIOR BALANCE:':20}", 'Rp. 'f'{balance_before:,}')
    print(f"{'PROFIT/LOSS:':20}", 'Rp. 'f'{balance - balance_before:,}')

    if balance>balance_before: 
        print(f"{'TRADE RESULT:':20}", 'PROFIT')
        trades_list.append(1)
    elif balance<balance_before: 
        print(f"{'TRADE RESULT:':20}", 'LOSS')
        trades_list.append(-1)
    elif balance==balance_before: 
        print(f"{'TRADE RESULT:':20}", 'DRAW')
        trades_list.append(0)

    print(f"\n{'TRADES COMPLETED:':20}", len(trades_list))
    print(f"OVERALL TRADE RESULTS:\n{trades_list}")
    print(f"OVERALL MARTINGALE RESULTS:\n{martingales_list}")

    return balance, trades_list, martingales_list

####################################################################################################################

def martingale(signal, op_list, m_level, m_max, m_switching):

    # check if current trade is profit or not
    start_time = time.time()
    earnings = read_earnings()

    # proceed martingale if earnings is 0
    if earnings==0:

        m_level += 1
        
        # if m_switching==True, open position's direction is opposite to the previous signal direction
        if m_switching==True:
            if signal==BUY: signal=SELL
            elif signal==SELL: signal=BUY
        
        open_position(signal, op_list[m_level], m_level)
        
        # make sure that no pop up is blocking
        # refresh()

        end_time = time.time()

        time.sleep(60 - (end_time - start_time))
        print(f"\n{'CHECK:':10}", datetime.now().strftime("%H:%M:%S"))

        # if martingale level is less than max martingale level, check for martingale again
        if m_level<m_max: m_level = martingale(signal, op_list, m_level, m_max, m_switching)

    return m_level

####################################################################################################################

def get_balance():

    pointer_click(BLANK)

    mouse.position = BALANCE
    time.sleep(0.1)
    mouse.click(mouse_button.left, 2)
    time.sleep(0.1)
    
    # copy selected content to clipboard
    with keyboard.pressed(copy_button): keyboard.press('c')
    pointer_click(BLANK)

    # paste latest clipboard content
    balance = pyperclip.paste()
    # remove non-numeric characters
    balance = ''.join(i for i in balance if i.isdigit() or i=='.')
    # convert to integers & return
    return int(float(str(balance)))
    
####################################################################################################################

def read_earnings():

    image = pyautogui.screenshot(region=SS_EARNINGS)
    image.save(PATH_EARNINGS)
    earnings = read_screenshot(PATH_EARNINGS)
    # print(f"\n{'EARNINGS:':20}", 'Rp. 'f'{earnings:,}')
    return earnings

####################################################################################################################

def read_rsi_stochastic():

    regions = [SS_RSI, SS_STOCHASTIC]
    paths = [PATH_RSI, PATH_STOCHASTIC]

    # regions = [SS_RSI, SS_STOCHASTIC, SS_PRICE]
    # paths = [PATH_RSI, PATH_STOCHASTIC, PATH_PRICE]

    for region in regions:
        image = pyautogui.screenshot(region=region)
        image.save(paths[ regions.index(region) ])
    
    rsi = read_screenshot(PATH_RSI)
    time.sleep(1)
    stochastic = read_screenshot(PATH_STOCHASTIC)
    # time.sleep(1)
    # price = read_screenshot(PATH_PRICE)

    print(f"{'RSI:':15}", rsi)
    print(f"{'Stochastic:':15}", stochastic)
    # print(f"{'Price:':15}", price)

    # return rsi, stochastic, price
    return rsi, stochastic

####################################################################################################################

def read_screenshot(path):

    # read image & standard preprocessing
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.bitwise_not(image)

    def crop_img(img, scale=1.0):
        center_x, center_y = img.shape[1]/2, img.shape[0]/2
        width_scaled, height_scaled = img.shape[1] * scale, img.shape[0] * scale
        left_x, right_x = center_x - width_scaled/2, center_x + width_scaled/2
        top_y, bottom_y = center_y - height_scaled/2, center_y + height_scaled/2
        img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
        return img_cropped

    def crop_left(img, scale=1.0):
        center_x, center_y = img.shape[1]/2, img.shape[0]/2
        width_scaled, height_scaled = img.shape[1] * scale, img.shape[0]
        width_unscaled = img.shape[1]
        left_x, right_x = center_x - width_scaled/2, center_x + width_unscaled/2
        top_y, bottom_y = center_y - height_scaled/2, center_y + height_scaled/2
        img_cropped = img[int(top_y):int(bottom_y), int(left_x):int(right_x)]
        return img_cropped

    if path==PATH_RSI or path==PATH_STOCHASTIC:

        # standard preprocessing & resize image
        retval, image = cv2.threshold(image, 100 , 255, cv2.THRESH_BINARY)
        image = cv2.resize(image, (100, 100), interpolation = cv2.INTER_CUBIC)

        # convert to gray, and threshold
        th, threshed = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)

        # morph-op to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
        morphed = cv2.morphologyEx(threshed, cv2.MORPH_CLOSE, kernel)

        # find the max-area contour
        cnts = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        cnt = sorted(cnts, key=cv2.contourArea)[-1]

        # crop and save it
        x,y,w,h = cv2.boundingRect(cnt)
        dst = img_cropped = image[y:y+h, x:x+w]
        img_cropped = crop_left(img_cropped, 0.6)
        img_cropped = crop_img(img_cropped, 0.8)
        cv2.imwrite(PATH_TEST, img_cropped)

        config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789'
        text = pytesseract.image_to_string(img_cropped, config=config)
        text = ''.join(i for i in text if i.isdigit())

        if len(text)>0: 
            text = int(text)
            if text>=0 and text<=100: return text
            else: end_program(error=True)
        else: end_program(error=True)

    elif path==PATH_EARNINGS or path==PATH_PRICE:

        # resize image & standard preprocessing
        image = cv2.resize(image,(0,0),fx=20,fy=20)
        retval, image = cv2.threshold(image, 100 , 255, cv2.THRESH_BINARY)
        # cv2.imwrite(PATH_TEST, image)

        if path==PATH_EARNINGS: config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789,.'
        elif path==PATH_PRICE: config = '--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789.'

        text = pytesseract.image_to_string(image, config=config)
        text = ''.join(i for i in text if i.isdigit() or i=='.')

        if len(text)>0: return float(text)
        else: end_program(error=True)

####################################################################################################################

def get_csv_data(strategy, m_max, balance):

    # collect data from csv file
    df = pd.read_csv(PATH_CSV, index_col=[0])

    # convert columns into lists
    col_date, col_time_start, col_time_end = list(df['Date']), list(df['Time Start']), list(df['Time End'])
    col_strategy, col_martingale_max = list(df['Strategy']), list(df['Martingale Max'])
    col_balance_start, col_balance_end = list(df['Starting Balance']), list(df['Ending Balance'])
    col_trades, col_martingales = list(df['Trades']), list(df['Martingales'])

    # add current trading data (before trade begin)
    col_date.append(datetime.now().strftime('%d/%m/%Y'))
    col_time_start.append(datetime.now().strftime('%H:%M:%S'))
    col_strategy.append(strategy)
    col_martingale_max.append(m_max)
    col_balance_start.append(balance)

    return [ col_date, col_time_start, col_time_end, col_strategy, col_martingale_max, 
             col_balance_start, col_balance_end, col_trades, col_martingales ]

####################################################################################################################

def set_csv_data(data, balance, trades_list, martingales_list):

    col_date, col_time_start, col_time_end, col_strategy, col_martingale_max, \
    col_balance_start, col_balance_end, col_trades, col_martingales = data

    # add current trading data (after trades end)
    if len(trades_list)==1:
        col_time_end.append(datetime.now().strftime('%H:%M:%S'))
        col_balance_end.append(balance)
        col_trades.append(trades_list)
        col_martingales.append(martingales_list)
    elif len(trades_list)>1:
        col_time_end[len(col_time_end)-1] = datetime.now().strftime('%H:%M:%S')
        col_balance_end[len(col_balance_end)-1] = balance
        col_trades[len(col_trades)-1] = trades_list
        col_martingales[len(col_martingales)-1] = martingales_list

    # override dataframe with additional new data
    df = pd.DataFrame()
    df['Date'], df['Time Start'], df['Time End'] = col_date, col_time_start, col_time_end
    df['Strategy'], df['Martingale Max'] = col_strategy, col_martingale_max
    df['Starting Balance'], df['Ending Balance'] = col_balance_start, col_balance_end

    # calculate profit & earning percentages for all data
    df['Profit'] = df['Ending Balance'] - df['Starting Balance']
    df['Profit (%)'] = ( df['Profit'] / df['Starting Balance'] ) * 100
    df['Profit (%)'] = df['Profit (%)'].round(2)

    # add new trades' data
    df['Trades'], df['Martingales'] = col_trades, col_martingales
    
    # save data to csv file
    df.to_csv(PATH_CSV)

####################################################################################################################

def end_program(error=False):

    if error==True: print("\nProgram Stopped: Error Reading")
    print("\nBINOBOT Ended....")
    print("Thank You for Using Our Program\n")
    sys.exit()

####################################################################################################################
