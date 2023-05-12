"""Directs actions based on command prompt from an MQTT topic"""

import json
import command_actions
from neopolitan_handler import command_map as neop_command
from connection_builder import publish
from const import OPERATIONS,RES_DATA_OPERATIONS,REQ_DATA_OPERATIONS,COMMAND_STREAM
from log import get_logger

# todo: this is stupid, we already separated by topic
def handle_subscription(topic, payload, mqtt_connection):
    """Delegates in incoming subscription"""
    logger = get_logger()
    logger.info('subscription: %s', topic)
    obj = json.loads(payload)
    response = None
    if topic == REQ_DATA_OPERATIONS:
        response = json.dumps({"res": OPERATIONS})
        response_topic = RES_DATA_OPERATIONS
    elif topic == COMMAND_STREAM:
        response,response_topic = parse_command(obj)
    else:
        logger.warning('Unrecognized topic: %s', topic)
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
    logger = get_logger()
    try:
        response_topic = obj['topic']
        action = obj['action']
        cmd = action['cmd']
        data = action['data']
        options = None
    except Exception as err:
        logger.warning('Could not parse obj: %s - %s', obj, err)
    try:
        options = action['options']
    except Exception as err:
        logger.warning('No options value - %s', err)
    result = command_switch(cmd, data, options)
    response = f'{result} command successfully processed' if result \
        else f'Error processing {result} command'
    return json.dumps(response),response_topic

def command_switch(cmd, data, options=None):
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
            # todo: is this bad?
            if options is not None:
                neop_func(options)
            else:
                neop_func()
            return f'Neopolitan[{data}] successfully sent'
        return f'Error sending Neopolitan[{data}]'
    if cmd == 'say':
        cmd = f'echo {data}'
        return command_actions.run_in_terminal(cmd)
    get_logger().warning('Unknown action: %s', cmd)
    return str(cmd)
