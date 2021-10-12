# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 14:47:14 2021

@author: baudr
"""

#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))#binding the adress and the port to the server
    s.listen()#waiting for the client to connect to the server
    print("waiting for client ...")
    conn, addr = s.accept()#connection with the client, getting infos about the client
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)#buffer size 1024, recieving the data send by the server
            if not data:
                break
            conn.sendall(data)#send to the client the data as soon as the server recieved it
