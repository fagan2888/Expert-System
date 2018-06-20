import bin.shunting_yard as shunting_yard
import sys


def parse_ipn(facts, ipn):
    nbr_fact = 0
    nbr_ope = 0
    for word in ipn:
        for letter in word:
            if 'A' <= letter <= 'Z':
                if letter not in facts:
                    facts[letter] = False
                nbr_fact += 1
            elif letter in ['+', '|', '^']:
                nbr_ope += 1
    return facts, nbr_fact, nbr_ope


def get_condition(elements):
    last, new_elems, ipn_condition = shunting_yard.create_ipn(elements)
    if not ipn_condition:
        return None, None
    if new_elems[0] not in ['<', '=']:
        return None, None
    return new_elems, ipn_condition


def get_queries_init(elements, facts):
    infos = []
    if len(elements[0]) == 1:
        del elements[0]
    else:
        elements[0] = elements[0][1:]
    for word in elements:
        for letter in word:
            if 'A' <= letter <= 'z':
                if letter not in facts:
                    print('Fact', letter, 'does not exist')
                    sys.exit(1)
                infos.append(letter)
            elif letter == '#':
                return infos
            else:
                return None
    return infos
