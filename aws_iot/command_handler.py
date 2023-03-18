"""Directs actions based on command prompt from an MQTT topic"""

import json
import command_actions

from connection_builder import publish



def handle_command(topic, payload):
    """Parses a JSON command payload"""
    # pylint: disable=unused-argument
    obj = json.loads(payload)
    action = obj['action']
    cmd = action['cmd']
    data = action['data']
    res = command_switch(cmd, data)
    # publish result
    # publish(None, res, json.dumps({res: "Command successfully processed"}))

def command_switch(cmd, data):
    """Delegates command action"""

    # todo: upgrade to Python 3.10 so we can use 'match'
    # pylint: disable=pointless-string-statement
    """match cmd:
        case 'print':
            print('action:', cmd, ('"' + data + '"'))
        case _:
            print('Unknown action:', cmd)"""

    if cmd == 'print':
        command_actions.print_message(data)
        return True
    print('Unknown action:', cmd)
    return False
