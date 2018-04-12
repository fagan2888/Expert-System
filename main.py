import sys
import bin.file_manager as file_man


def start():
    fd = file_man.open_file(sys.argv)
    file_man.parse_file(fd)


if __name__ == "__main__":
    start()
