"""Directs actions based on command prompt from an MQTT topic"""

import json
import logging
import command_actions
from neopolitan_handler import command_map as neop_command
from connection_builder import publish
from const import OPERATIONS,RES_DATA_OPERATIONS,REQ_DATA_OPERATIONS,COMMAND_STREAM

# todo: this is stupid, we already separated by topic
def handle_subscription(topic, payload, mqtt_connection):
    """Delegates in incoming subscription"""
    logging.info(f'subscription: {topic}')
    obj = json.loads(payload)
    response = None
    if topic == REQ_DATA_OPERATIONS:
        response = json.dumps({"res": OPERATIONS})
        response_topic = RES_DATA_OPERATIONS
    elif topic == COMMAND_STREAM:
        response,response_topic = parse_command(obj)
    else:
        logging.warning(f'Unrecognized topic: {topic}')
        return
    publish(mqtt_connection, response_topic, response)

# todo: redesign to be more like AWS doc
# pylint: disable=unused-argument
def data_switch(data):
    """Deal with data commands"""
    # pylint: disable=unnecessary-pass
    pass

def parse_command(obj):
    """Parses a JSON command payload"""
    response_topic = obj['topic']
    action = obj['action']
    cmd = action['cmd']
    data = action['data']
    result = command_switch(cmd, data)
    response = f'{result} command successfully processed' if result \
        else f'Error processing {result} command'
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
    if cmd == 'neopolitan':
        neop_func = neop_command(data)
        if neop_func:
            neop_func()
            return f'Neopolitan[{data}] successfully sent'    
        else:
            return f'Error sending Neopolitan[{data}]'
    if cmd == 'say':
        cmd = f'echo {data}'
        return command_actions.run_in_terminal(cmd)
    logging.warning(f'Unknown action: {cmd}')
    return str(cmd)
