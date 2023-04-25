"""Honestly can't remember"""

import threading
from awscrt import io, mqtt # , auth, http
from awsiot import mqtt_connection_builder




class AWSListener:

    # Security key directory
    CERTS_DIR = '/home/jay/Desktop/credentials/aws/iot/'
    # AWS endpoint
    ENDPOINT = None  
    # ToDo: title?
    CLIENT_ID = 'Hubble'
    # ToDo: title?
    CERT = CERTS_DIR + 'Hubble.cert.pem'
    # Private AWS connection key
    KEY = CERTS_DIR + 'Hubble.private.key'
    # ToDo: title?
    ROOT_CA = CERTS_DIR + 'root-CA.crt'

    def __init__(self):
        # --- local vars ---
        # disconnection (stop) event
        self.disconnect_event = None
        # AWS mqtt connection for pub/sub
        self.mqtt_connection = None
        # ------------------

        # Get endpoint from file
        with open(AWSListener.CERTS_DIR + 'endpoint.txt', 'r') as endpoint_file:
            AWSListener.ENDPOINT = endpoint_file.readline()
            endpoint_file.close()
        # Initialize disconnection event
        self.disconnect_event = threading.Event()

    # Default callback when subscribed messages are received
    def on_message_received(topic, payload):
        print("Received message from topic '{}': {}".format(topic, payload))
    
    # Disconnection callback
    def disconnect_callback(self, topic, payload):
        print('Received disconnection topic event')   
        self.disconnect_event.set()

    # Subscribe to a topic
    def subscribe(self, topic, callback=on_message_received):
        # Subscribe
        print("Subscribing to topic '{}'...".format(topic))
        subscribe_future, packet_id = self.mqtt_connection.subscribe(
            topic=topic,
            qos=mqtt.QoS.AT_LEAST_ONCE,
            callback=callback)
        subscribe_result = subscribe_future.result()
        print("Subscribed with {}".format(str(subscribe_result['qos'])))

    # Connect to AWS
    def connect(self):
        # Create a connection to AWS
        def create_connection():
            # Spin up resources
            event_loop_group = io.EventLoopGroup(1)
            host_resolver = io.DefaultHostResolver(event_loop_group)
            client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
            mqtt_connection = mqtt_connection_builder.mtls_from_path(
                        endpoint=AWSListener.ENDPOINT,
                        cert_filepath=AWSListener.CERT,
                        pri_key_filepath=AWSListener.KEY,
                        client_bootstrap=client_bootstrap,
                        ca_filepath=AWSListener.ROOT_CA,
                        client_id=AWSListener.CLIENT_ID,
                        clean_session=False,
                        keep_alive_secs=6
                        )
            self.mqtt_connection = mqtt_connection
            print('Mqtt connection created')
        
        if not self.mqtt_connection:
            print('No mqtt connection, creating...')
            create_connection()

        print("Connecting to {} with client ID '{}'...".format(
                AWSListener.ENDPOINT, AWSListener.CLIENT_ID))
        # Make the connect() call
        connect_future = self.mqtt_connection.connect()
        # Future.result() waits until a result is available
        connect_future.result()
        print('Connected successfully')

    # Disconnect from AWS
    def disconnect(self):
        print('Disconnecting')
        disconnect_future = self.mqtt_connection.disconnect()
        disconnect_future.result()
        print('Disconnected successfully')

    # Listens for messages until receiving a stop event
    def listen_then_disconnect(self):
        print('Subscribing to disconnection callback')
        self.subscribe('state', callback=self.disconnect_callback)
        while not self.disconnect_event.is_set():
            pass
        self.disconnect()      


listener = AWSListener()
listener.connect()
listener.subscribe('t1')
listener.listen_then_disconnect()