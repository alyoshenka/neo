from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

import json
import threading

CERTS_DIR = '/home/jay/Desktop/credentials/aws/iot/'

ENDPOINT = None
# ToDo: put this somewhere else
with open(CERTS_DIR + 'endpoint.txt', 'r') as endpoint_file:
    ENDPOINT = endpoint_file.readline()
    endpoint_file.close()
CLIENT_ID = 'Hubble'
CERT = CERTS_DIR + 'Hubble.cert.pem'
KEY = CERTS_DIR + 'Hubble.private.key'
ROOT_CA = CERTS_DIR + 'root-CA.crt'

disconnect_event = threading.Event()

def on_connection_interrupted():
    print("Connection interrupted")

def on_connection_resumed():
    print("Connection resumed")

def on_resubscribe_complete():
    print("Resubscribe complete")

# not sure why this takes 2 args?
def on_message_received(topic, payload):
    print("Received message from topic '{}': {}".format(topic, payload))

# Create a connection to AWS
def create_connection():
    # Spin up resources
    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
    mqtt_connection = mqtt_connection_builder.mtls_from_path(
                endpoint=ENDPOINT,
                cert_filepath=CERT,
                pri_key_filepath=KEY,
                client_bootstrap=client_bootstrap,
                ca_filepath=ROOT_CA,
                client_id=CLIENT_ID,
                clean_session=False,
                keep_alive_secs=6
                )
    return mqtt_connection

# Connect to AWS
def connect(mqtt_connection):
    print("Connecting to {} with client ID '{}'...".format(
            ENDPOINT, CLIENT_ID))
    # Make the connect() call
    connect_future = mqtt_connection.connect()
    # Future.result() waits until a result is available
    connect_future.result()
    print("Connected!")

# Subscribe to a topic
def subscribe(mqtt_connection, topic, callback=on_message_received):
    # Subscribe
    print("Begin Subscribe")
    print("Subscribing to topic '{}'...".format(topic))
    subscribe_future, packet_id = mqtt_connection.subscribe(
        topic=topic,
        qos=mqtt.QoS.AT_LEAST_ONCE,
        callback=callback)
    subscribe_result = subscribe_future.result()
    print("Subscribed with {}".format(str(subscribe_result['qos'])))
    print("Subscribe End")

def state_callback(topic, payload):
    print('Received state topic event')   
    disconnect_event.set()

def disconnect(mqtt_connection):
    print("Disconnecting")
    disconnect_future = mqtt_connection.disconnect()
    disconnect_future.result()
    print("Disconnected")

if __name__ == '__main__':
    
    mqtt_connection = create_connection()
    connect(mqtt_connection)   
    subscribe(mqtt_connection, 't1')
    subscribe(mqtt_connection, 'state', callback=state_callback)

    # ToDo: redo this; figure out how to do better
    while disconnect_event.is_set():
        pass
    disconnect_event.wait()
    print('Disconnect event received and processed. Disconnection...')

    disconnect(mqtt_connection)    