"""Subscribes to topic 'sub_topic', listens for 20s, then exits"""

# pylint: disable=unused-import

import time as t
from connection_builder import create_mqtt_connection, subscribe, publish, disconnect
from command_handler import handle_command


PUB_TOPIC = 'test' # Topic to publish to
MESSAGE = 'hello!' # message to send
COMMAND_STREAM = 'cmd/neo/neopolitan/hubble/console/req'

def main(wait=100):
    """Main application function"""
    mqtt_connection = create_mqtt_connection()
    subscribe(mqtt_connection, COMMAND_STREAM,
              on_message_received=lambda topic,payload :
              handle_command(topic,payload,mqtt_connection))
    # publish(mqtt_connection, PUB_TOPIC, MESSAGE)
    t.sleep(wait) # Keep the connection alive for 20s
    disconnect(mqtt_connection)

if __name__ == '__main__':
    main()
