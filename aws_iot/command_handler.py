"""Directs actions based on command prompt from an MQTT topic"""

import json
import command_actions
from connection_builder import publish


# pylint: disable=unused-argument
def handle_command(topic, payload, mqtt_connection):
    """Parses a JSON command payload"""
    obj = json.loads(payload)
    response_topic = obj['topic']
    action = obj['action']
    cmd = action['cmd']
    data = action['data']
    result = command_switch(cmd, data)
    response = "Command successfully processed" if result else "Error processing command"
    # publish result
    publish(mqtt_connection, response_topic, json.dumps({"res": response}))

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
    if cmd == 'run':
        if data == 'neopixeltest':
            command_actions.run_neopixel_test()
            return True
    print('Unknown action:', cmd)
    return False
