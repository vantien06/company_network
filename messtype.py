from enum import Enum
"""
    define the type of messages that could be sent
    between the server and the client or client and client
"""
class mess_type(Enum):
    HANDSHAKE = 1
    REQUEST = 2
    RESPONSE = 3
    PEER_REQUEST = 4
    PEER_RESPONSE = 5
    PEER_UPDATE_REQUEST = 6
    PEER_UPDATE_RESPONSE = 7
    SERVER_UPDATE_REQUEST = 8
    SERVER_UPDATE_RESPONSE = 9
    CLOSE = 10
    