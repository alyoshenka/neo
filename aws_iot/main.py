"""Main application program"""

# pylint: disable=unused-import

import time as t
from connection_builder import create_mqtt_connection, disconnect
from setup import initialize_subscriptions


def main(wait=10):
    """Main application function"""
    mqtt_connection = create_mqtt_connection()
    initialize_subscriptions(mqtt_connection)
    # todo: make continuously listen
    t.sleep(wait) # Keep the connection alive for 10s
    disconnect(mqtt_connection)

if __name__ == '__main__':
    main()
