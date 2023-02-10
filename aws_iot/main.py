"""Subscribes to topic 'sub_topic', listens for 20s, then exits"""


import time as t
from connection_builder import create_mqtt_connection, subscribe, publish, disconnect


PUB_TOPIC = 'test' # Topic to publish to
MESSAGE = 'hello!' # message to send
SUB_TOPIC = "sub_topic" # topic to subscribe to

def main(wait=20):
    """Main application function"""
    mqtt_connection = create_mqtt_connection()
    subscribe(mqtt_connection, SUB_TOPIC)
    publish(mqtt_connection, PUB_TOPIC, MESSAGE)
    t.sleep(wait) # Keep the connection alive for 20s
    disconnect(mqtt_connection)

if __name__ == '__main__':
    main()
