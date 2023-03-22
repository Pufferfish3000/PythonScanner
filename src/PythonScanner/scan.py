#!/usr/bin/env python3
"""
Main scanner functions

@author: Byrnes
"""

import socket


def checkPort(source, port):
    # specifies an tcp port over an ipv4 address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # attempts to connect to port
    try:
        s.connect((source, port))
        return "connection established"
    # if fails output error
    except socket.error as error:
        return (error)
    # close connection
    finally:
        s.close()


def tcpScan(target):
    for port in range(1, 90):
        # specifies an tcp port over an ipv4 address
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # times out socket objects after one second
        socket.setdefaulttimeout(1)

        # checks if can successfully connect to port
        if (s.connect_ex((target, port)) == 0):
            print("port: " + str(port) + " is open")
