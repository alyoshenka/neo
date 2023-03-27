"""Directs actions based on command prompt from an MQTT topic"""

import json
import command_actions
from connection_builder import publish
from const import OPERATIONS,DATA_OPERATIONS,REQ_DATA_OPERATIONS,COMMAND_STREAM

# todo: this is stupid, we already separated by topic
def handle_subscription(topic, payload, mqtt_connection):
    """Delegates in incoming subscription"""
    obj = json.loads(payload)
    response = None
    if topic == REQ_DATA_OPERATIONS:
        response = json.dumps({"res": OPERATIONS})
        response_topic = DATA_OPERATIONS
    elif topic == COMMAND_STREAM:
        response,response_topic = parse_command(obj)
    else:
        print(f'Unrecognized topic: {topic}')
        return 
    publish(mqtt_connection, response_topic, response)

# todo: redesign to be more like AWS doc
def data_switch(dt):
    pass
    

def parse_command(obj):
    """Parses a JSON command payload"""
    response_topic = obj['topic']
    action = obj['action']
    cmd = action['cmd']
    data = action['data']
    result = command_switch(cmd, data)
    response = f'{result} command successfully processed' if result \
        else f'Error processing {result}command'
    return json.dumps(response),response_topic

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
        return f'print {data}'
    if cmd == 'run':
        if data == 'neopixeltest':
            command_actions.run_neopixel_test()
            return 'run neopixeltest'
    print('Unknown action:', cmd)
    return str(cmd)
