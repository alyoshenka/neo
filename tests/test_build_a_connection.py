"""Tests building the MQTT connection"""

from aws_iot.connection_builder import create_mqtt_connection, disconnect

def test_build_connection():
    """Tests that an MQTT connection can be built without errors"""
    try:
        mqtt_connection = create_mqtt_connection()
    except Exception as err:
        print(err)
        assert False
    disconnect(mqtt_connection)
    