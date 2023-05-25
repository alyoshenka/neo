"""Definitions"""

# Data listener
# DATA_STREAM = "dt/neo/req" # still not what we want
DATA_OPERATIONS = 'dt/neo/operations/hubble'
REQ_DATA_OPERATIONS = DATA_OPERATIONS + '/req'
RES_DATA_OPERATIONS = DATA_OPERATIONS + '/res'
# Command listener
COMMAND_STREAM = 'cmd/neo/hubble'
COMMAND_STREAM_REQ = COMMAND_STREAM + '/req'
COMMAND_STREAM_RES = COMMAND_STREAM + '/res'

# todo: make this better
# Things this program can be told to do
OPERATIONS = [
    {
        "module": "neopolitan",
        "subCommand": "test",
        "friendlyName": "Run Neopolitan Test"
    },
    {
        "module": "neopolitan",
        "subCommand": "open",
        "friendlyName": "Open Neopolitan Display"
    },
    {
        "module": "neopolitan",
        "subCommand": "close",
        "friendlyName": "Close Neopolitan Display"
    },
    {
        "module": "neopolitan",
        "subCommand": "update",
        "friendlyName": "Update Neopolitan Display",
        "options": {'say': None, 'speed': None, 'wrap': None}
    },
    {
        "module": "run",
        "subCommand": "other-thing",
        "friendlyName": "Run 'other-thing'"
    },
    {
        "module": "print",
        "data": "hello",
        "friendlyName": "Print 'hello'"
    }
]
