import socket
from enum import Enum

PIECE_SIZE = 150
CODE = 'utf-8'
host_ip='10.255.255.255'
port=1
#def get_ip_add()
def get_ip_addr():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #greekforgreek
    try:
        s.connect((host_ip, port))
        IP = s.getsockname()[0]
        print("test1")
    except:
        IP = '127.0.0.1'
        print("test2")
    finally:
        print("test3")
        s.close()
    return IP
#define message could be sent between 
# client and server or client and client
class message(Enum):
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
    