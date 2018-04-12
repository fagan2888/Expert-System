import sys
import logging
import shunting_yard
import facts_manager

logging.basicConfig(filename='info.txt', level=logging.DEBUG)


def find_errors(elements, ipn, line_nb):
    if elements[0][0] == '#' and ipn:
        print('You forgot to set a conclusion at line %d' % line_nb)
        sys.exit(1)
    elif elements[0][0] == '=' and len(elements[0]) > 1 and elements[0][1] != '>' and ipn:
        print('No facts must be given before the initial facts at line %d' % line_nb)
        sys.exit(1)
    elif elements[0][0] == '?' and ipn:
        print('No facts must be given before the query at line %d' %line_nb)
        sys.exit(1)
    elif elements[0][0] not in ['<', '=', '#', '?']:
        print('Syntax error at line %d: %s' % (line_nb, elements[0]))
        sys.exit(1)


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


def parse_file(fd):
    facts = []
    with fd:
        for line_nb, line in enumerate(fd):
            elements = line.split()
            idx_word, idx_letter, ipn_statement = shunting_yard.create_ipn(elements)
            del elements[0:idx_word]
            elements[0] = elements[0][idx_letter:]
            find_errors(elements, ipn_statement, line_nb)
            if elements[0][0:2] == '=>':
                if len(elements[0]) > 2:
                    elements[0] = elements[0][2:]
                else:
                    del elements[0]
                idx_word, idx_letter, ipn_conclusion = shunting_yard.create_ipn(elements)

                #facts = facts_manager.create_fact(facts, elements, ipn, line_nb)

    for i in facts:
        print(i.name)
        for j in i.ipn:
            print(j)


def start():
    fd = open_file(sys.argv)
    parse_file(fd)


if __name__ == "__main__":
    start()
