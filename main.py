import bin.inference as inference
import bin.file_manager as file_manager
import sys
import os


def start():
    fd = file_manager.open_file(sys.argv)
    #fd = open(os.getcwd() + '/tests/simpletest')
    facts, graph, queries, init = file_manager.parse_file(fd)
    fd.close()
    inference.inference(facts, graph, queries, init)


if __name__ == "__main__":
    start()
