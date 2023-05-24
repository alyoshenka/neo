"""Setup functions"""
from const import COMMAND_STREAM_REQ, REQ_DATA_OPERATIONS
from subscription_handler import handle_operation_request, handle_command_request
from connection_builder import subscribe
from routes import publish_available_operations

def initialize_subscriptions(mqtt_connection):
    """Subscribe to data and command streams"""
    # todo: is this necessary?
    subscribe(mqtt_connection, REQ_DATA_OPERATIONS,
        on_message_received=lambda topic,payload :
        handle_operation_request(topic,payload,mqtt_connection))
    subscribe(mqtt_connection, COMMAND_STREAM_REQ,
              on_message_received=lambda topic,payload :
              handle_command_request(topic,payload,mqtt_connection))

def initial_publish(mqtt_connection):
    """Publishing that happens on startup"""
    publish_available_operations(mqtt_connection)
