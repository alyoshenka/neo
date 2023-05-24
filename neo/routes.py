"""Manages subscriptions to specified topics"""

from const import RES_DATA_OPERATIONS, OPERATIONS
from connection_builder import publish

def publish_available_operations(mqtt_connection, topic=RES_DATA_OPERATIONS):
    """Publishes available operations to the correct topic"""
    publish(mqtt_connection, topic, {"availableOperations": OPERATIONS})
