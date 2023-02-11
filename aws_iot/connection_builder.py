"""Handles building connections to AWS via MQTT protocol"""

import os
import json
from awscrt import io, mqtt # , auth, http
from awsiot import mqtt_connection_builder
from dotenv import load_dotenv


# todo: callbacks
def create_mqtt_connection():
    """Initializes the connection to AWS"""

    # Load secrets
    client_id = 'Hubble'
    load_dotenv()
    try:
        endpoint = os.environ['ENDPOINT']
        # convert to bytes
        cert =     str.encode(os.environ['HUBBLE_CERT_PEM'])
        key =      str.encode(os.environ['HUBBLE_PRIVATE_KEY'])
        root_ca =  str.encode(os.environ['ROOT_CA_CRT'])
    except Exception as err:
        print('error loading env vars:', err)
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

    print(f'Connecting to {endpoint} with client ID: "{client_id}"...')
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")

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

# not sure why this takes 2 args?
def on_message_received(topic, payload):
    """Callback for when a message is received"""
    print(f'Received message from topic "{topic}": {payload}')

def publish(mqtt_connection, topic, message):
    """Publish a message to a topic"""
    # Publish message to server desired number of times.
    print('Begin Publish')
    data = f'{message}'
    message = {"message" : data}
    mqtt_connection.publish(topic=topic, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + json.dumps(message) + "' to the topic: " + topic)
    print('Publish End')

def subscribe(mqtt_connection, topic):
    """Subscribe to a topic"""
    print(f'Subscribing to topic "{topic}"...')
    # pylint: disable=unused-variable
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=on_message_received)
    subscribe_result = subscribe_future.result()
    print(f'Subscribed with: {(subscribe_result["qos"])}')

def disconnect(mqtt_connection):
    """Disconnect"""
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected")
