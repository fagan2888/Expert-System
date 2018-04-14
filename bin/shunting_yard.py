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


def create_ipn(elements):
    ipn = []
    stack = []
    for idx_word, word in enumerate(elements):
        for idx_letter, letter in enumerate(word):
            if 'A' <= letter <= 'Z':
                ipn.append(letter)
            elif letter in ['(', ')', '+', '|', '^', '!']:
                manage_stack(letter, ipn, stack)
            else:
                while stack:
                    ipn.append(stack.pop())
                return idx_word, idx_letter, ipn
    return len(elements), 0, ipn
