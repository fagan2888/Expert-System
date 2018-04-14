import sys
import bin.parsing as parsing

def open_file(argv):
    try:
        assert len(argv) == 2
        file_name = argv[1]
        fd = open(file_name, "r")
    except AssertionError:
        print("Expert system takes one argument only")
        sys.exit(1)
    except FileNotFoundError:
        print("This file does not exist")
        sys.exit(1)
    return fd


def start():
    fd = open_file(sys.argv)
    facts, rules = parsing.parse_file(fd)


if __name__ == "__main__":
    start()
