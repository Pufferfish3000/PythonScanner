#!/usr/bin/env python3
""" Contains the classes to be used by control.py to conduct port scanning

@author: Byrnes 
"""

import socket

class PortScanner:
    """
    A class representing a port scan

    ...

    Attributes
    ----------
    target : str
        A ipv4 address or domain that will be the target of the scan

    Methods
    -------
    checkTcpPort(port)
        Determines if a port is open
    tcpScan()
        Conducts a tcp connect scan on target
    """

    def __init__(self, target):
        """
        Parameters
        ----------
        target : str
            A ipv4 address or domain that will be the target of the scan

        Returns
        -------
        None

        """

        self.target = target

    def checkTcpPort(self, port):
        """ Determines if a port is open

        Parameters
        ----------
        port : int
            The port that is having its state checked

        Returns
        -------
        port : int
            Open ports

        """

        # specifies a tcp port over a ipv4 address
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # times out socket objects after one quarter second
        socket.setdefaulttimeout(.25)

        # checks if can successfully connect to port
        if (s.connect_ex((self.target, port)) == 0):
            return port
        return -1

    def tcpScan(self):
        """ Conducts a tcp connect scan on a target

        Returns
        -------
        openPorts : list
            open ports

        """

        openPorts = []
        # conducts a tcp connect scan on ports one through ninety
        for port in range(1, 90):
            checkedPort = self.checkTcpPort(port)
            if checkedPort != -1:
                openPorts.append(str(checkedPort))
        return openPorts

class Output:

    def __init__(self, data, path):
        self.data = data
        self.path = path

    def outputToTerminal(self):
        print(' '.join(self.data))

    def outputToFile(self):
        try:
            f = open(self.path, "w")
            f.write(' '.join(self.data))
            f.close()
            print("successfully wrote to " + self.path)
        except:
            print("an error occured when writing to " + self.path)