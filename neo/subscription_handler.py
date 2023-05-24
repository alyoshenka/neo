"""Directs actions based on command prompt from an MQTT topic"""

import json
import command_actions
from neopolitan_handler import command_map as neop_command
from connection_builder import publish
from const import OPERATIONS,RES_DATA_OPERATIONS,REQ_DATA_OPERATIONS,\
    COMMAND_STREAM_REQ,COMMAND_STREAM_RES
from log import get_logger
from routes import publish_available_operations

# pylint: disable=broad-except

def handle_command_request(topic, payload, mqtt_connection):
    """Handles an incoming command from `COMMAND_STREAM`"""
    assert topic == COMMAND_STREAM_REQ, \
        'This function should only receive subscriptions from `COMMAND_STREAM`'
    response,response_topic = execute_command(json.loads(payload))
    get_logger().info('publishing %s to %s', response, response_topic)
    publish(mqtt_connection, response_topic, response)

# pylint: disable=inconsistent-return-statements
def handle_operation_request(topic, payload, mqtt_connection):
    """Handles a request for available operations"""
    assert topic == REQ_DATA_OPERATIONS, \
        'This function should only receive subscriptions from `REQ_DATA_OPERATIONS`'
    logger = get_logger()
    logger.info('Data operations were requested')
    response_topic = RES_DATA_OPERATIONS

    try:
        obj = json.loads(payload)
        if 'responseTopic' in obj:
            logger.info('Requested with non-default response topic: %s', obj['responseTopic'])
            response_topic = obj['responseTopic']
    except Exception as err:
        logger.warning('Payload cannot be loaded into JSON: %s - %s', payload, err)

    publish_available_operations(mqtt_connection, topic=response_topic)

# todo: redesign to be more like AWS doc
# pylint: disable=unused-argument
def data_switch(data):
    """Deal with data commands"""
    # pylint: disable=unnecessary-pass
    pass

def execute_command(obj):
    """Parses a JSON command payload and then executes the specified command. \
    Returns the response and response topic, if specified."""
    logger = get_logger()
    try:
        response_topic = obj['responseTopic']
    except Exception as err:
        logger.warning('Could not get responseTopic from %s: %s', obj, err)
        response_topic = COMMAND_STREAM_RES
    result = command_switch(obj)
    response = f'{result} command successfully processed' if result \
        else None
    return json.dumps({"commandResponse": response}),response_topic

# pylint: disable=no-else-return
# pylint: disable=too-many-return-statements
def command_switch(obj):
    """Delegates command action"""

    logger = get_logger()

    # todo: upgrade to Python 3.10 so we can use 'match'
    # pylint: disable=pointless-string-statement
    """match cmd:
        case 'print':
            print('action:', cmd, ('"' + data + '"'))
        case _:
            print('Unknown action:', cmd)"""

    try:
        module = obj['module']
    except Exception as err:
        logger.warning('Object has no command module: %s - %s', obj, err)
        return None

    if module == 'neopolitan':
        try:
            sub_command = obj['subCommand']
        except Exception as err:
            logger.warning('neopolitan action has no subCommand: %s - %s', obj, err)
            return None
        neop_func = neop_command(sub_command)
        if neop_func:
            if sub_command == 'update': # todo: handle more funcs with args
                try:
                    options = obj['options']
                    neop_func(options)
                except Exception as err:
                    logger.warning('No options specified for update command: %s - %s', obj, err)
                    return None
            else:
                neop_func()
            return f'Neopolitan[{obj}] successfully sent'
        else:
            logger.info('Error sending Neopolitan[%s]', obj)
            return None
    if module == 'print':
        try:
            data = module['data']
            command_actions.print_message(data)
            return f'printed {data}'
        except Exception as err:
            logger.warning('Module has no data: %s - %s', module, err)
            return None
    if module == 'terminal':
        try:
            sub_command = module['subCommand']
            return command_actions.run_in_terminal(sub_command)
        except Exception as err:
            logger.warning('Module has no subCommand: %s - %s', module, err)
            return None

    logger.warning('Unable to process command module: %s', module)
    return None
