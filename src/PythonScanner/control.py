#!/usr/bin/env python3
"""
Main controller

@author: Byrnes
"""

import argparse
import scan


def main():
    """
    gathers input from user to determine what functions to run
    """

    parser = argparse.ArgumentParser(description="Simple tcp and udp scanner")
    outputMethod = parser.add_mutually_exclusive_group()

    parser.add_argument("address", type=str,
                        help="The ipv4 address or domain of your target")
    parser.add_argument("--tcp-scan", "-t", action="store_true",
                          dest="tcpScan", help="Tcp connect scan")
    outputMethod.add_argument("--output-terminal", "-o", action="store_true", 
                        dest="terminal", help="outputs open ports to terminal")
    outputMethod.add_argument("--output-file", "-f", type=str, 
                        dest="file", help="outputs open ports to file")
    args = parser.parse_args()

    scanner = scan.PortScanner(args.address)

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
