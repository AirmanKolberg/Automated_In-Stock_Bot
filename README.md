# Automated_In-Stock_Bot
This bot was designed to automate a task very important to me, monitoring GPUs and ASIC miners to see when they'll be in stock.  Using this simple script (Selenium and Twilio required), you can effortlessly allow this bot to keep an eye out for when the next- whatever it is- is in stock!  🤙🏼

Thankfully, this can all be done in the background, as I've added options in selenium to prevent a web broswer from presenting itself on the screen.  Feel free to also change what happens whenever something comes in stock (ie a function that buys it for you, or perhaps opens the site in a browser, etc.).  Enjoy!

Steps for a Successful Setup:
- Ensure you can run Python scripts
- pip (or pip3) install both selenium and twilio
- Set up a Twilio account (free on their website) and insert necessary information into secrets.py
- Add a list of links and out-of-stock tags in secrets.py (examples given)
- python3 main.py and you're good to go!

If, for any reason, you would like to donate- though unneccesary, is always apreciated!

BitCoin: 3Gj49JGVPXjw3994bSebQNrHsFJkZE9iRg && Etherium: 0x08b57537943BBb6A527C9c861E9550D9Be9f7729

Thank you all for reading!
