"""Definitions"""

# Data listener
# DATA_STREAM = 'dt/neo/req' # still not what we want
DATA_OPERATIONS = 'dt/neo/operations/hubble'
REQ_DATA_OPERATIONS = DATA_OPERATIONS + '/req'
RES_DATA_OPERATIONS = DATA_OPERATIONS + '/res'
# Command listener
COMMAND_STREAM = 'cmd/neo/hubble/req'

# todo: make this better
# Things this program can be told to do
OPERATIONS = [
    {
        'cmd': 'neopolitan', 
        'data': 'test', 
        'friendlyName': 'Run Neopolitan Test' 
    }, # todo: make simpler?
        {
        'cmd': 'neopolitan', 
        'data': 'open', 
        'friendlyName': 'Open Neopolitan Display' 
    },
    {
        'cmd': 'neopolitan', 
        'data': 'close', 
        'friendlyName': 'Close Neopolitan Display' 
    },
    {
        'cmd': 'neopolitan', 
        'data': 'update', 
        'friendlyName': 'Update Neopolitan Display (not impl)' 
    },
    {
        'cmd': 'run', 
        'data': 'other-thing', 
        'friendlyName': 'Run "other-thing"' 
    },
    {
        'cmd': 'print', 
        'data': 'hello', 
        'friendlyName': 'Print "hello"' 
    }
]
