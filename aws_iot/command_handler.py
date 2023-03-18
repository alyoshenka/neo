import json
import command_actions

from connection_builder import publish

# not sure why this takes 2 args?
# todo: what action should this take?
def print_message_received(topic, payload):
    """Callback for when a message is received"""
    print(f'Received message from topic "{topic}": {payload}; returning')

def handle_command(topic, payload):
    """Parses a JSON command payload"""
    obj = json.loads(payload)
    action = obj['action']
    cmd = action['cmd']
    data = action['data']
    res = command_switch(cmd, data)
    # publish result
    publish(None, res, json.dumps({res: "Command successfully processed"}))
    

def command_switch(cmd, data):
    """Delegates command action"""

    # todo: upgrade to Python 3.10 so we can use 'match'
    """match cmd:
        case 'print':
            print('action:', cmd, ('"' + data + '"'))
        case _:
            print('Unknown action:', cmd)"""
    
    if cmd == 'print':
        command_actions.print_message(data)
        return True
    else:
        print('Unknown action:', cmd)
        return False
