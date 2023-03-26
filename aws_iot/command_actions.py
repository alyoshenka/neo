"""Capabilities of this program; what actions it can do"""

import os

import sys
import subprocess

def print_message(msg):
    """Print a message to the console"""
    print('print command:', msg)

def run_neopixel_test():
    """Runs a program that displays a simple animation on the LED board"""
    # os.system('neopixeltest')
    # subprocess.call('neopixeltest')
    print('Recieved "neopixeltest" command')
    sp = subprocess.Popen(["/bin/bash", "-i", "-c", 'neopixeltest'])
    sp.communicate()

# not sure why this takes 2 args?
# todo: what action should this take?
# todo: wrong place?
def print_message_received(topic, payload):
    """Callback for when a message is received"""
    print(f'Received message from topic "{topic}": {payload}; returning')
