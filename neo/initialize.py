"""Setup functions"""
import json
from const import COMMAND_STREAM, REQ_DATA_OPERATIONS, RES_DATA_OPERATIONS, OPERATIONS
from subscription_handler import handle_subscription
from connection_builder import subscribe, publish

def initialize_subscriptions(mqtt_connection):
    """Subscribe to data and command streams"""
    # todo: is this necessary?
    subscribe(mqtt_connection, REQ_DATA_OPERATIONS,
        on_message_received=lambda topic,payload :
        handle_subscription(topic,payload,mqtt_connection))
    subscribe(mqtt_connection, COMMAND_STREAM,
              on_message_received=lambda topic,payload :
              handle_subscription(topic,payload,mqtt_connection))

def initial_publish(mqtt_connection):
    """Publishing that happens on startup"""
     # todo: take out res?
    publish(mqtt_connection, RES_DATA_OPERATIONS, json.dumps({"res": OPERATIONS}))