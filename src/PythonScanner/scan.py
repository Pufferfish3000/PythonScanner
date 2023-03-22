#!/usr/bin/env python3
"""
Main scanner functions

@author: Byrnes
"""

import socket

def checkPort(source, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        s.connect((source, port))
        return (True)
    except socket.error as error:
        return (False)
    finally:
        s.close()