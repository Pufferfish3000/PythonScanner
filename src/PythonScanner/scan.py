#!/usr/bin/env python3
""" Contains the classes to be used by control.py to conduct port scanning and display output

    PortScanner
        Scans tcp ports using a tcp connect scan. Contains methods to scan a single
        port, or ports 1 through 90. Methods return any open ports
    Output
        Outputs data to a terminal or file. Formats output as port numbers with
        spaces to not interfere with any tools using the output
    
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
        for port in range(1, 91):
            checkedPort = self.checkTcpPort(port)
            if checkedPort != -1:
                openPorts.append(str(checkedPort))
        return openPorts


class Output:
    """ A class representing the diffrent types of output that a user can choose

    Outputs only the port numbers to increase flow when piped into other functions

    ...

    Attributes
    ----------
    data : str
        Relevant data to be outputted
    path : str
        Path and file type for an output file

    Methods
    -------
    outputToTerminal()
        Outputs data to Terminal
    outputToFile()
        Conducts a tcp connect scan on target
    """

    def __init__(self, data, path):
        """
        Parameters
        ----------
        data : str
            Relevant data to be outputted
        path : str
            Path and file type for an output file

        Returns
        -------
        None.

        """
        self.data = data
        self.path = path

    def outputToTerminal(self):
        """ Outputs data to terminal

        Returns
        -------
        None.

        """
        print(' '.join(self.data))

    def outputToFile(self):
        """ Outputs data to a file 

        Returns
        -------
        None.

        """
        try:
            f = open(self.path, "w")
            f.write(' '.join(self.data))
            f.close()
            print("successfully wrote to " + self.path)
        except:
            print("an error occured when writing to " + self.path)
