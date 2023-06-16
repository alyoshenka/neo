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
# Heartbreat listener
HEARTBEAT_REQ = 'dt/neo/heartbeat/req'
HEARTBEAT_RES = 'dt/neo/heartbeat/res'

# todo: make this better
# Things this program can be told to do
OPERATIONS = [
    {
        "module": "neopolitan",
        "subCommand": "open",
        "friendlyName": "Open Neopolitan Display",
        "group": "major"
    },
    {
        "module": "neopolitan",
        "subCommand": "close",
        "friendlyName": "Close Neopolitan Display",
        "group": "major"
    },
    {
        "module": "neopolitan",
        "subCommand": "update",
        "friendlyName": "Update Neopolitan Display",
        "options": {'say': None, 'speed': None, 'wrap': None},
        "group": "major"
    },
    {
        "module": "neopolitan",
        "subCommand": "test",
        "friendlyName": "Run Neopolitan Test",
        "group": "test"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAll",
        "friendlyName": "Display All Symbols",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllLowercase",
        "friendlyName": "Display Lowercase Letters",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllUppercase",
        "friendlyName": "Display Uppercase Letters",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllNumbers",
        "friendlyName": "Display All Numbers",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "displayAllSymbols",
        "friendlyName": "Display All Symbols",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "colorDemo",
        "friendlyName": "Display Color Demo",
        "group": "demo"
    },
    {
        "module": "neopolitan",
        "subCommand": "stockTicker",
        "friendlyName": "Default Tickers",
        "group": "wowFactor"
    },
    {
        "module": "neopolitan",
        "subCommand": "stockTickerSNP",
        "friendlyName": "S&P 500",
        "group": "wowFactor"
    },
    {
        "module": "neopolitan",
        "subCommand": "stockTickerNASDAQ",
        "friendlyName": "NASDAQ 100",
        "group": "wowFactor"
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
