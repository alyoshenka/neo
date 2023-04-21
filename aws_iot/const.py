"""Definitions"""

# Data listener
# DATA_STREAM = 'dt/neo/req' # still not what we want
DATA_OPERATIONS = 'dt/neo/operations/hubble'
REQ_DATA_OPERATIONS = DATA_OPERATIONS + '/req'
RES_DATA_OPERATIONS = DATA_OPERATIONS + '/res'
# Command listener
COMMAND_STREAM = 'cmd/neo/hubble/req'

# Things this program can be told to do
OPERATIONS = [
    { 'cmd': 'run', 'data': 'neopixeltest', 'friendlyName': 'Run Neopixeltest' }, # todo: make simpler?
    { 'cmd': 'run', 'data': 'other-thing', 'friendlyName': 'Run "other-thing"' },
    { 'cmd': 'print', 'data': 'hello', 'friendlyName': 'Print "hello"' }
]
