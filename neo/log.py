"""Initializes the logger with a custom name"""

import logging
import datetime
import os

def init_logger():
    """Set up the log file"""
    if not os.path.exists('logs/'):
        os.makedirs('logs/')
    filename = 'logs/neo ' + str(datetime.datetime.now()) + '.txt'
    logging.basicConfig(filename=filename, encoding='utf=8', level=logging.DEBUG)

def get_logger():
    """Get the logger for this application"""
    return logging.getLogger('neo')
