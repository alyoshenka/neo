"""
Sets up display for a simple stock ticker

Note that this file is for demo purposes only,
    and will eventually be abstracted into its own repository
"""

import yfinance as yf
from neopolitan.board_functions.colors import GREEN, RED
from neopolitan.demos import display

TICKERS = ["tsla", "uber", "wmt", "ko", "tgt", "orcl", "sbux", "aapl"]
UP = '↑'
DOWN = '↓'

def run(events):
    """Run the stock ticker"""
    display(construct_message(), events)

def construct_message():
    """Constructs the data to send to neopolitan to display stocks"""
    all_ticker_data = [get_ticker_data(sym) for sym in TICKERS]
    msg = []
    for tick in all_ticker_data:
        msg.append(('  ' + ticker_obj_to_string(tick), GREEN if tick['up?'] else RED))
    return msg

def get_ticker_data(sym):
    """"Query and return formatted data from a ticker symbol"""
    try:
        data = yf.Ticker(str(sym))
    except Exception as err:
        print("ERROR", err)
        return None

    info = data.info
    #hist = data.history(period='5d')
    
    close = info['previousClose']
    #openP = info['open']
    #high = info['dayHigh']
    #low = info['dayLow']
    cur = info['currentPrice']
    name = info['shortName']
    symbol = info['symbol']

    delta = cur - close

    obj = {
        "symbol": symbol,
        "name": name,
        "dollarDelta": round(delta, 2),
        "percentDelta": round(delta/close*100, 2),
        "up?": delta > 0
    }
    return obj

def ticker_obj_to_string(obj):
    """Converts a ticker object into a nice display string"""
    arrow = UP if obj["up?"] else DOWN
    dollar = '{0:.2f}'.format(obj["dollarDelta"])
    percent = '{0:.2f}'.format(obj["percentDelta"])
    return f'{obj["symbol"]} {arrow} ${dollar} {percent}%'
