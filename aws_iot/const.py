"""Definitions"""

# Data listener
# DATA_STREAM = 'dt/neo/req' # still not what we want
DATA_OPERATIONS = 'dt/neo/operations'
REQ_DATA_OPERATIONS = DATA_OPERATIONS + '/req'
# Command listener
COMMAND_STREAM = 'cmd/neo/req'

# Things this program can be told to do
OPERATIONS = [
    { 'cmd': 'run', 'data': 'neopixeltest' }, # todo: make simpler?
    { 'cmd': 'run', 'data': 'other-thing' },
    { 'cmd': 'print', 'data': 'hello from AWS'}
]
