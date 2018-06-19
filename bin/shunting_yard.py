def update_ipn(letter, stack, ipn, priorities):
    while stack and stack[-1] in priorities:
        ipn.append(stack.pop())
    stack.append(letter)


def manage_stack(letter, ipn, stack, new):
    priorities = ['^', '|', '+', '!']
    if letter == '(':
        stack.append(letter)
    elif letter == ')':
        if not new:
            return False
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
    return True


def create_ipn(elements):
    ipn = []
    stack = []
    new = False
    for idx_word, word in enumerate(elements):
        for idx_letter, letter in enumerate(word):
            if 'A' <= letter <= 'Z':
                ipn.append(letter)
                new = True
            elif letter in ['(', ')', '+', '|', '^', '!']:
                if not manage_stack(letter, ipn, stack, new):
                    return 0, 0, None
                new = False
            else:
                while stack:
                    ret = stack.pop()
                    if ret == '(':
                        return 0, 0, None
                    ipn.append(ret)
                return idx_word, idx_letter, ipn
    while stack:
        ipn.append(stack.pop())
    return len(elements), 0, ipn
