"""Setup functions"""
from const import *
from subscription_handler import handle_subscription
from connection_builder import subscribe

def initialize_subscriptions(mqtt_connection):
    """Subscribe to data and command streams"""
    subscribe(mqtt_connection, REQ_DATA_OPERATIONS,
              on_message_received=lambda topic,payload :
              handle_subscription(topic,payload,mqtt_connection))
    subscribe(mqtt_connection, COMMAND_STREAM,
              on_message_received=lambda topic,payload :
              handle_subscription(topic,payload,mqtt_connection))