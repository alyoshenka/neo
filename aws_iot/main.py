"""Subscribes to topic 'sub_topic', listens for 20s, then exits"""

# pylint: disable=fixme
# todo: fixme

import time as t
from connection_builder import create_mqtt_connection, subscribe, publish, disconnect



PUB_TOPIC = 'test' # Topic to publish to
MESSAGE = 'hello!' # message to send

SUB_TOPIC = "sub_topic" # topic to subscribe to



MQTT_CONNECTION = create_mqtt_connection()
subscribe(MQTT_CONNECTION, SUB_TOPIC)
publish(MQTT_CONNECTION, PUB_TOPIC, MESSAGE)
t.sleep(20) # Keep the connection alive for 20s
disconnect(MQTT_CONNECTION)
