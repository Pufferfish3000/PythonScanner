#!/usr/bin/env python3
""" Output

@author: Byrnes 
"""


class Output:

    def __init__(self, data, path):
        self.data = data
        self.path = path

    def outputToTerminal(self):
        print(' '.join(self.data))
