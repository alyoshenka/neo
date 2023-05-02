"""Capabilities of this program; what actions it can do"""
# todo: better explanation^

import subprocess
import logging
from neopolitan_handler import test_display

def print_message(msg):
    """Print a message to the console"""
    print('print command:', msg)

def run_neopixel_test():
    """Runs a program that displays a simple animation on the LED board"""
    # print('Recieved "neopixeltest" command')
    try:
        test_display()
    # pylint: disable=bare-except
    except:
        logging.warning('Could not open neopolitan display')
        return 'Could not open neopolitan display'
    return 'neopolitan test successfuly run'

def run_in_terminal(cmd):
    """Runs a command in a command line environment"""
    #with subprocess.check_output(["/bin/bash", "-i", "-c", cmd]) as sub:
        #sub.communicate()
    try:
        subprocess.run(["/bin/bash", "-c", cmd], check=True)
    except subprocess.CalledProcessError as err:
        return f'{cmd} command error: {err}'
    return f'command "{cmd}" successfuly processed'

# not sure why this takes 2 args?
# todo: what action should this take?
# todo: wrong place?
def log_message_received(topic, payload):
    """Callback for when a message is received"""
    logging.info(f'Received message from topic "{topic}": {payload}')
