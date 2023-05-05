"""Initializes the logger with a custom name"""

import logging
import datetime

def init_logger():
    """Set up the log file"""
    filename = 'logs/neo_' + str(datetime.datetime.now()) + '.txt'
    logging.basicConfig(filename=filename, encoding='utf=8', level=logging.DEBUG)

logger = logging.getLogger('neo')
