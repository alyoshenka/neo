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
        "subCommand": "open",
        "friendlyName": "o Open Neopolitan Display"
    },
    {
        "module": "neopolitan",
        "subCommand": "close",
        "friendlyName": "x Close Neopolitan Display"
    },
    {
        "module": "neopolitan",
        "subCommand": "update",
        "friendlyName": "u Update Neopolitan Display",
        "options": {'say': None, 'speed': None, 'wrap': None}
    },
    {
        "module": "neopolitan",
        "subCommand": "test",
        "friendlyName": "t Run Neopolitan Test"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAll",
        "friendlyName": "- Display All Symbols"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllLowercase",
        "friendlyName": "- Display Lowercase Letters"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllUppercase",
        "friendlyName": "- Display Uppercase Letters"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllNumbers",
        "friendlyName": "- Display All Numbers"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllSymbols",
        "friendlyName": "- Display All Symbols"
    },
    {
        "module": "neopolitan",
        "subCommand": "colorDemo",
        "friendlyName": "* Display Color Demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "stockTicker",
        "friendlyName": "$ Run Stock Ticker"
    }
]

"""
{
    "module": "run",
    "subCommand": "other-thing",
    "friendlyName": "Run 'other-thing'"
},
{
    "module": "print",
    "data": "hello",
    "friendlyName": "Print 'hello'"
},
    """
