import re
import sys

class fact(object):

    def __init__(self, name):
        self.name = name
        self.on = False
        self.rule = []

def start():
    file_name = sys.argv[1]
    with open(file_name, "r") as fd:
        for line in fd:
            print("Line = %s" % line)


if __name__ == "__main__":
    start()
