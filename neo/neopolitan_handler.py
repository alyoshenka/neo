"""
Manages interactions with the display board

See testboardrunner.py for an example:
    https://github.com/alyoshenka/neopolitan/blob/main/neopolitan/testboardrunner.py
"""
# pylint: disable=global-statement

from threading import Thread
from queue import Queue
import time
import logging
from neopolitan.neop import main as neop

# todo: is global var ok?
NEOPOLITAN_THREAD = None
EVENT_QUEUE = None

def command_map(data):
    """Returns the appropriate function"""
    if data == 'open':
        logging.info('Returning "neopolitan open" func')
        return open_display
    if data == 'close':
        logging.info('Returning "neopolitan close" func')
        return close_display
    if data == 'update':
        logging.info('Returning "neopolitan update" func')
        return update_display
    if data == 'test':
        logging.info('Returning "neopolitan test" func')
        return test_display
    logging.warning('No Neopolitan action found for: %s', data)
    return None

def open_display():
    """Open the neopolitan display. Should be blank""" # todo: initialize blank?
    logging.info('running open_display')

    global NEOPOLITAN_THREAD
    global EVENT_QUEUE
    if NEOPOLITAN_THREAD or EVENT_QUEUE:
        logging.warning('NEOPOLITAN_THREAD or EVENT_QUEUE already initialized')
        return

    EVENT_QUEUE = Queue()
    NEOPOLITAN_THREAD = Thread(target=neop, args=(EVENT_QUEUE,))
    NEOPOLITAN_THREAD.start()

def close_display():
    """Close the neopolitan display"""
    logging.info('running close_display')

    global NEOPOLITAN_THREAD
    global EVENT_QUEUE

    if not (EVENT_QUEUE and NEOPOLITAN_THREAD):
        logging.warning('EVENT_QUEUE or NEOPOLITAN_THREAD not initialized')
        return

    EVENT_QUEUE.put('exit')

    NEOPOLITAN_THREAD.join()

    NEOPOLITAN_THREAD = None
    EVENT_QUEUE = None

def update_display(options):
    """Send arguments to the display"""
    logging.info('running update_display')

    def parse_option(opt):
        """Handles a single option"""
        value = options[opt]
        if not value:
            logging.warning('No value passed in %s', opt)
            return
        if not EVENT_QUEUE:
            logging.warning('Event queue not initialized yet')
            return

        logging.info('adding to queue: %s=%s', opt, value)
        # todo: check if string. need to?
        put_str = str(opt) + ' ' + str(value)
        EVENT_QUEUE.put(put_str)

    for opt in options:
        parse_option(opt)

def test_display():
    """Test that events can be passed"""
    logging.info('running test_display')

    def wait_then_add(slp, evt):
        """Sleep for time then add argument to queue"""
        logging.info('Waiting for %s s then putting %s', slp, evt)
        time.sleep(slp)
        EVENT_QUEUE.put(evt)
    def wait_then_do(slp, func):
        """Sleep for time then run function"""
        if not callable(func):
            logging.warning('Passed an uncallable: %s', func)
            return
        logging.info('Waiting for %s s then doing %s', slp, func.__name__)

        time.sleep(slp)
        func()

    open_display()
    Thread(target=wait_then_add, args=(5, 'say beepboop')).start()
    Thread(target=wait_then_do, args=(10, close_display)).start()
