"""Capabilities of this program; what actions it can do"""

import subprocess

def print_message(msg):
    """Print a message to the console"""
    print('print command:', msg)

def run_neopixel_test():
    """Runs a program that displays a simple animation on the LED board"""
    print('Recieved "neopixeltest" command')
    with subprocess.Popen(["/bin/bash", "-i", "-c", 'neopixeltest']) as sub:
        sub.communicate()

# not sure why this takes 2 args?
# todo: what action should this take?
# todo: wrong place?
def print_message_received(topic, payload):
    """Callback for when a message is received"""
    print(f'Received message from topic "{topic}": {payload}; returning')
