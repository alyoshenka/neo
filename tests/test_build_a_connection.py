"""Tests building the MQTT connection"""

import logging
from neo.connection_builder import create_mqtt_connection, disconnect

def test_build_connection():
    """Tests that an MQTT connection can be built without errors"""
    try:
        mqtt_connection = create_mqtt_connection()
    # pylint: disable=broad-except
    except Exception as err:
        logging.error(err)
        assert False
    disconnect(mqtt_connection)
    