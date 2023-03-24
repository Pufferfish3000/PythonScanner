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
    scanType = parser.add_mutually_exclusive_group()
    parser.add_argument("address", type=str, dest="targetAddr",
                        help="The ipv4 address or domain of your target")
    scanType.add_argument("--tcp-scan", "-t", type=str, action="store_true",
                          dest="tcpScan", help="Tcp connect scan")
    scanType.add_argument("--udp-scan", "-u", type=str, action="store_true",
                          dest="udpScan", help="Udp scan")
    args = parser.parse_args()

    print(args)

    scanner = scan.PortScanner(args)


if __name__ == "__main__":
    main()
