"""Capabilities of this program; what actions it can do"""

import subprocess

def print_message(msg):
    """Print a message to the console"""
    print('print command:', msg)

def run_neopixel_test():
    """Runs a program that displays a simple animation on the LED board"""
    # print('Recieved "neopixeltest" command')
    try:
        with subprocess.check_output(['/bin/bash', '-c', "neopixeltest"]) as sub: # run()?
            sub.communicate()
    except subprocess.CalledProcessError as err:
        return f'"neopixel" command error: {err}'
    return 'command "neopixeltest" successfuly processed'

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
def print_message_received(topic, payload):
    """Callback for when a message is received"""
    print(f'Received message from topic "{topic}": {payload}; returning')
