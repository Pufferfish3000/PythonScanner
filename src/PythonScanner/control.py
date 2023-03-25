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
                        dest="tcpScan", help="Tcp connect scan")
    outputMethod.add_argument("--output-terminal", "-o", action="store_true",
                              dest="terminal", help="outputs open ports to terminal")
    outputMethod.add_argument("--output-file", "-f", type=str,
                              dest="file", help="outputs open ports to file")

    # stores relevant arguments in var args
    args = parser.parse_args()

    # new Port scanner object using ipv4 address supplied by the user
    scanner = scan.PortScanner(args.address)

    # runs methods based on relevant arguments
    if(args.tcpScan):
        out = scanner.tcpScan()
    if(args.terminal):
        outTerminal = scan.Output(out, "")
        outTerminal.outputToTerminal()
    if(args.file != None):
        outFile = scan.Output(out, args.file)
        outFile.outputToFile()


if __name__ == "__main__":
    main()
