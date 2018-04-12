import sys
import logging
import file_manager


logging.basicConfig(filename='info.txt', level=logging.DEBUG)








def start():
    fd = file_manager.open_file(sys.argv)
    file_manager.parse_file(fd)


if __name__ == "__main__":
    start()
