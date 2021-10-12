# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:06:04 2021

@author: baudr
"""

#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))# to connect to the server
    s.sendall(b'William Baudrand Chaudeyrac')#message that will be transfered (in binary form)
    data = s.recv(1024)# recieving the data send by the server, with a buffer of 1024

print('Received', repr(data))#printing the data recieved
