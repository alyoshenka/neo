# How Operations Work

## How do we publish the capabilities of this application?

The capabilities of this application are defined in `const.OPERATIONS`. 

When the program starts, it publishes these operations to `const.RES_DATA_OPERATIONS`, with the assumption that something is listening on the other side. In addition, the program subscribes to `const.REQ_DATA_OPERATIONS` so that when something else publishes to this topic to request the operations, this program can answer. 
See `initialize.py` for implementation.

## How do we interpret commands and perform the requisite functionality?

On startup, the program subscribes to `const.COMMAND_STREAM` to listen for command requests. Upon receiving a command, the payload is parsed and operations are performed based on its value.

This system is not entirely perfect, but it works for now.