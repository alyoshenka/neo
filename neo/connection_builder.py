"""Handles building connections to AWS via MQTT protocol"""

import os
import json
# pylint: disable=import-error
from awscrt import io, mqtt # , auth, http
from awsiot import mqtt_connection_builder
from dotenv import load_dotenv
from command_actions import log_message_received
from log import get_logger

# todo: callbacks
def create_mqtt_connection():
    """Initializes the connection to AWS"""

    logger = get_logger()

    # Load secrets
    load_dotenv()
    try:
        client_id   = os.environ['CLIENT_ID']
        endpoint    = os.environ['ENDPOINT']
        # convert to bytes
        cert    = str.encode(os.environ['CERT_PEM'])
        key     = str.encode(os.environ['PRIVATE_KEY'])
        root_ca = str.encode(os.environ['ROOT_CA_CRT'])
    except Exception as err:
        logger.error('error loading env vars: %s', err)
        return None

    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_bytes(
        endpoint=endpoint,
        cert_bytes=cert,
        pri_key_bytes=key,
        client_bootstrap=client_bootstrap,
        ca_bytes=root_ca,
        client_id=client_id,
        clean_session=False,
        keep_alive_secs=6)
    assert mqtt_connection is not None, 'MQTT connection not initialized'

    logger.info('Connecting to %s with client ID: "%s"...', endpoint, client_id)
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    logger.info("Connected!")

    return mqtt_connection

def on_connection_interrupted():
    """Callback for when connection is interrupted"""
    print("Connection interrupted")

def on_connection_resumed():
    """Callback for when connection is resumed"""
    print("Connection resumed")

def on_resubscribe_complete():
    """Callback for when resubscribe is complete"""
    print("Resubscribe complete")

def publish(mqtt_connection, topic, payload):
    """Publish a message to a topic"""
    # Publish message to server desired number of times.
    mqtt_connection.publish(topic=topic,
                            payload=json.dumps(payload),
                            qos=mqtt.QoS.AT_LEAST_ONCE)
    get_logger().info('Data: %s was published to: %s', str(payload), topic)

def subscribe(mqtt_connection, topic, on_message_received=log_message_received):
    """Subscribe to a topic"""
    assert mqtt_connection is not None, 'mqtt connection must be initialized'
    # pylint: disable=unused-variable
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received)
    subscribe_result = subscribe_future.result()
    get_logger().info('Subscribed to: %s', topic)

def disconnect(mqtt_connection):
    """Disconnect"""
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    get_logger().info("Disconnected")
