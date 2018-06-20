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
        if not stack:
            return False
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


def erase_multiple_neg(elements):
    cpy = []
    for word in elements:
        for letter in word:
            if letter == '!' and len(cpy) > 1 and cpy[-1] == '!':
                cpy.pop()
            else:
                cpy.append(letter)
    return cpy


def create_ipn(elements):
    ipn = []
    stack = []
    new = False
    new_elems = erase_multiple_neg(elements)
    for idx_letter, letter in enumerate(new_elems):
            if 'A' <= letter <= 'Z':
                ipn.append(letter)
                new = True
            elif letter in ['(', ')', '+', '|', '^', '!']:
                if not manage_stack(letter, ipn, stack, new):
                    return 0, 0, None
                if letter != ')':
                    new = False
            else:
                while stack:
                    ret = stack.pop()
                    if ret == '(':
                        return 0, 0, None
                    ipn.append(ret)
                return letter, new_elems[idx_letter:], ipn
    while stack:
        ret = stack.pop()
        if ret == '(':
            return 0, 0, None
        ipn.append(ret)
    return None, None, ipn
