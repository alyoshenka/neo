"""Tests subscribe and publish on local device"""

# todo: abstract json usage into utils file
import json
from aws_iot.connection_builder import \
    create_mqtt_connection, disconnect, publish, subscribe

HAS_RECEIVED = False

def test_sub_then_pub():
    """Builds an mqtt connection, 
        subscribes to a topic, 
        publishes to the same topic, 
        then verifies the response"""

    topic = "test_send_value"
    value = 20

    # pylint: disable=unused-argument
    def get_payload(topic, payload):
        """Get payload value"""
        message = json.loads(payload)
        assert int(message['message']) == value
        # pylint: disable=global-statement
        global HAS_RECEIVED
        HAS_RECEIVED = True

    mqtt_connection = create_mqtt_connection()
    subscribe(mqtt_connection, topic, on_message_received=get_payload)
    publish(mqtt_connection, topic, value)
    while not HAS_RECEIVED:
        continue
    disconnect(mqtt_connection)
