Python Artificial Intelligence Binary Options Trading Bot


Important Notice: 

- Before moving further, please be aware that Binary Options is an extremely
  risky way to make money. Over 95% of all Binary Options traders lose money, 
  and never made it back.

- This project shall only used for demo and educational purposes only, not
  for trading using real money.

- Feel free to test out the codes on your DEMO Account. However, it is HIGHLY 
  NOT RECCOMENDED to run the following program on your REAL trading account.

- To understand deeper regarding the trading strategies used by this AI bot, 
  please kindly do research on the following topics on behalf of Binary Options:
  - Target Profit
  - Stop Loss
  - Open Position / Bet Amount
  - Martingale Strategy (Levels and Amounts Calculation)


Python Libraries (Requirements):

- pandas
- numpy
- pyautogui
- pynput
- pytesseract
- pyperclip
- cv2
- PIL
- datetime
- time
- sys
- random


Initial Setup:

1. Create an account and/login to Binomo (Binary Options trading platform) on 
   your preffered web browser.

2. Install & run Visual Studio Code on your computer.

3. Install Pytesseract (Pre-packaged Computer Vision API) on your computer

4. Clone the GitHub repository to your computer, and open it on Visual Studio 
   Code

5. Make sure that all of the directories in the "variables.py" file are correct 
   these includes:
   - Path to the installed Pytesseract API
   - Path to the screenshots directories, which will be used for computer vision
   - Path to the CSV file which saves the bot's overall trading actions & results

6. Open both Visual Studio Code and the Browser running Binomo windows 
   side-by-side, similar like in the demo video: https://youtu.be/D9q4O8emVC4. 
   - Resize it so that both Visual Studio Code, and Binomo in the browser, are
     clearly visible, especially the main features of the trading platform.
   - Make sure that no user interfaces are covered/blocked by either one of the 
     windows.
   - Choose RSI(2) and Stochastic(4,3,3) as indicators on Binomo.
   - Set overbought and oversold lines at 80 and 20 respectively, for both
     indicators.
   - Select 30 seconds time-frame.

7. Use "test_coords.py" file to determine all coordinates of buttons and/or screen
   areas of the Binomo platform (browser) window:
   - Required buttons & screen areas are listed as variables in the "variables.py" 
     file. 
   - Once all coordinates are determined, fill them to their respective variables
     in the "variables.py" file.
   - Trial & errors may be required

8. Use "test_ss.py" file to determine all screenshot regions within the Binomo 
   platform (browser) window; these screenshots will be used for computer vision:
   - Required screenshot regions are listed as variables in the "variables.py" 
     file. 
   - Once all screenshot regions are determined, fill them to their respective 
     variables in the "variables.py" file.
   - Trial & errors will be required


How to Run:

1. Open both Visual Studio Code and the Browser running Binomo windows 
   side-by-side, similar like in the demo video: https://youtu.be/D9q4O8emVC4. 
   - Resize it so that both Visual Studio Code, and Binomo in the browser, are
     clearly visible, especially the main features of the trading platform.
   - Make sure that no user interfaces are covered/blocked by either one of the 
     windows.
   - Choose RSI(2) and Stochastic(4,3,3) as indicators on Binomo.
   - Set overbought and oversold lines at 80 and 20 respectively, for both
     indicators.
   - Select 30 seconds time-frame.

2. Set the following based on your preffered trading budget, by filling out their 
   respective variables, located on the uppermost few lines of the "main.py" file:
   - Open position amount (percentage of trading balance)
   - Target profit percentage (percentage of trading balance)
   - Stop loss percentage (percentage of trading balance)
   - Maximum levels of Martingale/s to be used by the bot
   - Type of Martingale Strategy (switching directions or not)
   - Martingale value (real number)

3. Pick a strategy to be used by the bot, currently there are 2 different trading 
   strategies offered, both could be used with/without Martingale:
   - Golden Moment: Bot will wait for a trading moment:
     - Call Signal (Upwards Direction): 
       - Both RSI and Stochastic indicators were below oversold lines on the 
         previous candle.
       - RSI of the current candle crosses to above the oversold line.
     - Put Signal (Downwards Direction):
       - Both RSI and Stochastic indicators were above overbought lines on the 
         previous candle.
       - RSI of the current candle crosses to below the overbought line.
   - Random: Bot will open position on random directions (gambling).
   - To pick a strategy, simply uncomment it, and comment the other strategy out
     on the "main.py" file

4. Bot will automatically stop trading if either one of the following occurs:
   - Balance reaches exactly or above target profit.
   - Balance reaches exactly or below stop loss limit.
   - The program experiences errors reading the screenshots, thereby stops itself
     to prevent unprecedented losses.
   
5. Enjoy...