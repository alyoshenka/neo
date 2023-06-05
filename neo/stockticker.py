"""
Sets up display for a simple stock ticker

Note that this file is for demo purposes only,
    and will eventually be abstracted into its own repository
"""

from threading import Thread
# pylint: disable=import-error
import yfinance as yf
from neopolitan.board_functions.colors import GREEN, RED
from neopolitan.board_functions.board_data import default_board_data
from neopolitan.naples import Neopolitan
from neopolitan.const import HEIGHT, WIDTH
from neopolitan.writing.data_transformation import dispatch_str_or_lst
from log import init_logger

TICKERS = ['tsla', 'uber', 'wmt', 'tgt', 'orcl', 'sbux', 'aapl', 'pep']
UP = '↑'
DOWN = '↓'
MIN_LEN = WIDTH * HEIGHT * 3 # todo: make sure works when scroll fast
TICKER_IDX = 2 # 3?

def monitor_message_length(neop):
    """Monitors how much of a message is left, and fetches the next ticker if it is time"""
    # pylint: disable=global-statement
    global TICKER_IDX # bad? yeah probably
    while not neop.display.should_exit:
        if len(neop.board.data) < MIN_LEN:
            next_sym = TICKERS[TICKER_IDX]
            TICKER_IDX += 1
            if TICKER_IDX >= len(TICKERS):
                TICKER_IDX = 0
            next_ticker = get_ticker_data(next_sym) # todo: next ticker, not static
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
    # thread that checks board data length
    #   query new data when it gets too low
    thrd = Thread(target=monitor_message_length, args=(neop,))
    thrd.start()

    neop.loop()

    thrd.join()
    # todo: maybe this one should delete itself?
    del neop

def construct_message():
    """Constructs the data to send to neopolitan to display stocks"""
    all_ticker_data = [get_ticker_data(sym) for sym in TICKERS[0:TICKER_IDX]]
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
