import sys
import logging
import shunting_yard

logging.basicConfig(filename='info.txt', level=logging.DEBUG)


class Fact(object):
    def __init__(self, name):
        self.name = name
        self.on = False
        self.ipn = []


def parse_line(line):
    elements = line.split()
    ipn, idx = shunting_yard.create_ipn(elements)

    print("\n")
    print(elements[idx])

    return ipn


def start():
    try:
        assert len(sys.argv) == 2
        file_name = sys.argv[1]
        fd = open(file_name, "r")
    except AssertionError:
        print("Il faut un et un seul argument")
        sys.exit(1)
    except FileNotFoundError:
        print("This file does not exist")
        sys.exit(1)
    with fd:
        for line in fd:
            print(parse_line(line))


if __name__ == "__main__":
    start()
