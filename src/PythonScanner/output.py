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

    def outputToFile(self):
        try:
            f = open(self.path, "w")
            f.write(' '.join(self.data))
            f.close()
        except:
            print("an error occured when writing to " + self.path)
