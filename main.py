import sys
import logging

logging.basicConfig(filename='info.txt', level=logging.DEBUG)


class Fact(object):
    def __init__(self, name):
        self.name = name
        self.on = False
        self.ipn = []


def update_ipn(letter, stack, ipn, priorities):
    while stack and stack[-1] in priorities:
        ipn.append(stack.pop())
    stack.append(letter)


def manage_stack(letter, ipn, stack):
    priorities = ['^', '|', '+', '!']
    if letter == '(':
        stack.append(letter)
    elif letter == ')':
        while stack and stack[-1] != '(':
            ipn.append(stack.pop())
        del stack[-1]
    elif letter == '!':
        update_ipn(letter, stack, ipn, priorities[3:])
    elif letter == '+':
        update_ipn(letter, stack, ipn, priorities[2:])
    elif letter == '|':
        update_ipn(letter, stack, ipn, priorities[1:])
    elif letter == '^':
        update_ipn(letter, stack, ipn, priorities)


def empty_stack(ipn, stack):
    while stack:
        ipn.append(stack.pop())


# Meilleure organisation avec operators ! Vire tout ca
def create_ipn(elements):
    ipn = []
    stack = []
    operators = ['(', ')', '!', '+', '|', '<', '=', '>', '^', '?']
    for idx, word in enumerate(elements):
        for letter in word:
            if letter == '#':
                empty_stack(ipn, stack)
                return ipn, idx
            try:
                assert ('A' <= letter <= 'Z') or letter in operators
            except AssertionError:
                print('Unknown character %c', letter)
                sys.exit(1)
            if letter in ['(', ')', '+', '|', '^', '!']:
                manage_stack(letter, ipn, stack)
            elif 'A' <= letter <= 'Z':
                ipn.append(letter)
            elif letter in ['<', '=', '>']:
                empty_stack(ipn, stack)
                return ipn, idx
    return ipn


def parse_line(line):
    elements = line.split()
    ipn, idx = create_ipn(elements)
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
