"""Main application program"""

# pylint: disable=unused-import

import time as t
from connection_builder import create_mqtt_connection, disconnect
from initialize import initialize_subscriptions, initial_publish
from log import init_logger, get_logger

def main(wait=100):
    """Main application function"""
    init_logger()
    logger = get_logger()

    logger.info('Starting the application')
    mqtt_connection = create_mqtt_connection()
    assert mqtt_connection is not None
    initialize_subscriptions(mqtt_connection)
    initial_publish(mqtt_connection)
    logger.info('Application has been set up and is now listening')
    # todo: listen for keyboardinterrupt , or other quit mechanism
    while True:
        t.sleep(0.5)
    t.sleep(wait) # Keep the connection alive
    disconnect(mqtt_connection)

if __name__ == '__main__':
    main()
