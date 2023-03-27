#!/usr/bin/env python3
"""
Main controller

@author: Byrnes
"""

import argparse
import scan


def main():
    """ Runs functions based on user input

    Returns
    -------
    None.

    """

    # arg parse object to simplify options
    parser = argparse.ArgumentParser(description="Simple tcp scanner")
    outputMethod = parser.add_mutually_exclusive_group()

    parser.add_argument("address", type=str,
                        help="The ipv4 address or domain of your target")
    parser.add_argument("--tcp-scan", "-t", action="store_true",
                        dest="tcpScan", default=True,
                        help="Tcp connect scan, default scan if not specified")
    outputMethod.add_argument("--output-terminal", "-o", default=True, action="store_true",
                              dest="terminal",
                              help="outputs open ports to terminal, default output if not specified")
    outputMethod.add_argument("--output-file", "-f", type=str,
                              dest="file", help="outputs open ports to file")

    # stores relevant arguments in var args
    args = parser.parse_args()

    # new Portscanner object using ipv4 address supplied by the user
    scanner = scan.PortScanner(args.address)

    # checks for any arguments and runs if necessary

    # checks to see if user used tcpScan argument
    if(args.tcpScan):
        # runs tcp connect scan on target address specified in scanner object,
        # then stores open ports in variable out
        out = scanner.tcpScan()

     # checks if user used file argment
    if(args.file != None):
        # creates a new Output object with open ports for data argument and a
        # str stored in args.file as the file path
        outFile = scan.Output(out, args.file)
        # calls outputToFile method
        outFile.outputToFile()

    # checks if user used termianal argument
    elif(args.terminal):
        # creates a new Output object with open ports for data argument and an
        # empty string for the path argument
        outTerminal = scan.Output(out, "")
        # calls outputToTerminal method
        outTerminal.outputToTerminal()


# executes when run as a script
if __name__ == "__main__":
    main()
