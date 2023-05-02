"""
Manages interactions with the display board

See testboardrunner.py for an example:
    https://github.com/alyoshenka/neopolitan/blob/main/neopolitan/testboardrunner.py
"""
# pylint: disable=global-statement

from threading import Thread
from queue import Queue
import time
from neopolitan.neop import main as neop

# todo: is global var ok?
NEOPOLITAN_THREAD = None
EVENT_QUEUE = None

def command_map(data):
    """Returns the appropriate function"""
    if data == 'open':
        return open_display
    if data == 'close':
        return close_display
    if data == 'update':
        return update_display
    if data == 'test':
        return test_display
    print(f'No Neopolitan action found for: {data}')
    return None

def open_display():
    """Open the neopolitan display. Should be blank"""
    # todo: only open if not open else error
    global NEOPOLITAN_THREAD
    global EVENT_QUEUE

    EVENT_QUEUE = Queue()
    NEOPOLITAN_THREAD = Thread(target=neop, args=(EVENT_QUEUE,))
    NEOPOLITAN_THREAD.start()

def close_display():
    """Close the neopolitan display"""
    global NEOPOLITAN_THREAD
    global EVENT_QUEUE

    EVENT_QUEUE.put('exit')

    NEOPOLITAN_THREAD.join()

    NEOPOLITAN_THREAD = None
    EVENT_QUEUE = None

def update_display():
    """Send arguments to the display"""

def test_display():
    """Test that events can be passed"""
    def wait_then_add(slp, evt):
        """Sleep for time then add argument to queue"""
        time.sleep(slp)
        EVENT_QUEUE.put(evt)
    def wait_then_do(slp, func):
        """Sleep for time then run function"""
        time.sleep(slp)
        func()

    open_display()
    Thread(target=wait_then_add, args=(5, 'say beepboop')).start()
    Thread(target=wait_then_do, args=(10, close_display)).start()
