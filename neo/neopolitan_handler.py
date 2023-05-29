"""
Manages interactions with the display board

See testboardrunner.py for an example:
    https://github.com/alyoshenka/neopolitan/blob/main/neopolitan/testboardrunner.py
"""
# pylint: disable=global-statement

from threading import Thread
from queue import Queue
import time
# pylint: disable=import-error
from neopolitan.neop import main as neop
from log import get_logger

# todo: is global var ok?
NEOPOLITAN_THREAD = None
EVENT_QUEUE = None

def command_map(data):
    """Returns the appropriate function"""
    logger = get_logger()
    if data == 'open':
        logger.info('Returning "neopolitan open" func')
        return lambda : open_display(neop)
    if data == 'close':
        logger.info('Returning "neopolitan close" func')
        return close_display
    if data == 'update':
        logger.info('Returning "neopolitan update" func')
        return update_display
    if data == 'test':
        logger.info('Returning "neopolitan test" func')
        return test_display
    logger.warning('No Neopolitan action found for: %s', data)
    return None

def open_display(func):
    """Open the neopolitan display. Should be blank""" # todo: initialize blank?
    logger = get_logger()
    logger.info('running open_display')

    global NEOPOLITAN_THREAD
    global EVENT_QUEUE
    if NEOPOLITAN_THREAD or EVENT_QUEUE:
        logger.warning('NEOPOLITAN_THREAD or EVENT_QUEUE already initialized')
        return

    EVENT_QUEUE = Queue()
    NEOPOLITAN_THREAD = Thread(target=func, args=(EVENT_QUEUE,))
    NEOPOLITAN_THREAD.start()

def close_display():
    """Close the neopolitan display"""
    logger = get_logger()
    logger.info('running close_display')

    global NEOPOLITAN_THREAD
    global EVENT_QUEUE

    if not (EVENT_QUEUE and NEOPOLITAN_THREAD):
        logger.warning('EVENT_QUEUE or NEOPOLITAN_THREAD not initialized')
        return

    EVENT_QUEUE.put('exit')

    NEOPOLITAN_THREAD.join()

    NEOPOLITAN_THREAD = None
    EVENT_QUEUE = None

def update_display(options):
    """Send arguments to the display"""
    logger = get_logger()
    logger.info('running update_display')

    def parse_option(opt):
        """Handles a single option"""
        value = options[opt]
        if not value:
            logger.warning('No value passed in %s', opt)
            return
        if not EVENT_QUEUE:
            logger.warning('Event queue not initialized yet')
            return

        logger.info('adding to queue: %s=%s', opt, value)
        # todo: check if string. need to?
        put_str = str(opt) + ' ' + str(value)
        EVENT_QUEUE.put(put_str)

    for opt in options:
        parse_option(opt)

def test_display():
    """Test that events can be passed"""
    logger = get_logger()
    logger.info('running test_display')

    def wait_then_add(slp, evt):
        """Sleep for time then add argument to queue"""
        logger.info('Waiting for %s s then putting %s', slp, evt)
        time.sleep(slp)
        EVENT_QUEUE.put(evt)
    def wait_then_do(slp, func):
        """Sleep for time then run function"""
        if not callable(func):
            logger.warning('Passed an uncallable: %s', func)
            return
        logger.info('Waiting for %s s then doing %s', slp, func.__name__)

        time.sleep(slp)
        func()

    open_display(neop)
    Thread(target=wait_then_add, args=(5, 'say beepboop')).start()
    Thread(target=wait_then_do, args=(10, close_display)).start()
