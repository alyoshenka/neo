"""
Manages interactions with the display board

See testboardrunner.py for an example:
    https://github.com/alyoshenka/neopolitan/blob/main/neopolitan/testboardrunner.py
"""
# pylint: disable=global-statement

from threading import Thread
from queue import Queue
from neopolitan.neop import main as neop

# todo: is global var ok?
NEOPOLITAN_THREAD = None
EVENT_QUEUE = None

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
