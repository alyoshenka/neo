from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

import json
import time as t

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

PUB_TOPIC = 'test 1'
MESSAGE = 'hello!'
RANGE = 0

SUB_TOPIC = "sub_topic"

def on_connection_interrupted():
    print("Connection interrupted")

def on_connection_resumed():
    print("Connection resumed")

def on_resubscribe_complete():
    print("Resubscribe complete")

# not sure why this takes 2 args?
def on_message_received(topic, payload):
    print("Received message from topic '{}': {}".format(topic, payload))

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


print("Connecting to {} with client ID '{}'...".format(
        ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")
# Publish message to server desired number of times.
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    mqtt_connection.publish(topic=PUB_TOPIC, payload=json.dumps(message), qos=mqtt.QoS.AT_LEAST_ONCE)
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/testing'")
    t.sleep(1)
print('Publish End')

# Subscribe
print("Begin Subscribe")
print("Subscribing to topic '{}'...".format(SUB_TOPIC))
subscribe_future, packet_id = mqtt_connection.subscribe(
    topic=SUB_TOPIC,
    qos=mqtt.QoS.AT_LEAST_ONCE,
    callback=on_message_received)
subscribe_result = subscribe_future.result()
print("Subscribed with {}".format(str(subscribe_result['qos'])))
print("Subscribe End")

t.sleep(20)

print("Disconnecting")
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()
print("Disconnected")