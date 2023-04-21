"""Main application program"""

# pylint: disable=unused-import

import time as t
from connection_builder import create_mqtt_connection, disconnect
from setup import initialize_subscriptions, initial_publish


def main(wait=100):
    """Main application function"""
    mqtt_connection = create_mqtt_connection()
    assert mqtt_connection is not None
    initialize_subscriptions(mqtt_connection)
    initial_publish(mqtt_connection)
    # todo: make continuously listen
    while True:
        t.sleep(0.5)
    t.sleep(wait) # Keep the connection alive
    disconnect(mqtt_connection)

if __name__ == '__main__':
    main()
