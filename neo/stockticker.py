"""
Sets up display for a simple stock ticker

Note that this file is for demo purposes only,
    and will eventually be abstracted into its own repository
"""

# pylint: disable=import-error
import yfinance as yf
from threading import Thread
import time
from neopolitan.board_functions.colors import GREEN, RED
from neopolitan.board_functions.board_data import default_board_data
from neopolitan.naples import Neopolitan
from neopolitan.const import HEIGHT, WIDTH
from neopolitan.writing.data_transformation import dispatch_str_or_lst
from log import init_logger

TICKERS = ["tsla", "uber", "wmt", "ko", "tgt", "orcl", "sbux", "aapl"]
TICKERS = ["tsla", "uber"]
UP = '↑'
DOWN = '↓'
MIN_LEN = WIDTH * HEIGHT * 3 # todo: make sure works when scroll fast

def monitor_message_length(neop):
    while not neop.display.should_exit:
        if len(neop.board.data) < MIN_LEN:
            next_ticker = get_ticker_data('wmt') # todo: next ticker, not static
            next_msg = \
                ('  ' + ticker_obj_to_string(next_ticker), \
                 GREEN if next_ticker['up?'] else RED)
            new_data = dispatch_str_or_lst([next_msg])
            neop.board.set_data(neop.board.data + new_data)

def run(events):
    """Run the stock ticker"""
    init_logger()

    board_data = default_board_data.copy()
    board_data.message = construct_message()
    board_data.should_wrap = False


    # board_data.scroll_fast()

    neop = Neopolitan(board_data=board_data, events=events)
    print(neop.board_data.should_wrap)
    # thread that checks board data length
    #   query new data when it gets too low
    t = Thread(target=monitor_message_length, args=(neop,))
    t.start()

    neop.loop()

    t.join()
    # todo: maybe this one should delete itself?
    del neop

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
    # pylint: disable=broad-except
    except Exception as err:
        print("ERROR", err)
        return None
    info = data.info
    close = info['previousClose']
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
    # pylint: disable=consider-using-f-string
    dollar = '{0:.2f}'.format(obj["dollarDelta"])
    percent = '{0:.2f}'.format(obj["percentDelta"])
    return f'{obj["symbol"]} {arrow} ${dollar} {percent}%'

run(None)
