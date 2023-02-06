"""Contains location information"""

# pylint: disable=fixme
# todo: do this better

# todo: secrets with python
CERTS_DIR = '/home/jay/Desktop/credentials/aws/iot/' # Where certificates are stored
# ENDPOINT = None # AWS endpoint
CLIENT_ID = 'Hubble' # Can be whatever
CERT = CERTS_DIR + 'Hubble.cert.pem' # Device certificate
KEY = CERTS_DIR + 'Hubble.private.key' # Private key
ROOT_CA = CERTS_DIR + 'root-CA.crt' # todo: what is this?
