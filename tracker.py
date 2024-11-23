import socket
import threading
import ast
import time

import server
from server import mess_type


SERVER_PORT = 12500
SERVER_IP = server.get_ip_address()
LISTEN_DURATION = 5
RECEIVE_SIZE = 1024
CODE = 'utf-8'

#class server:

