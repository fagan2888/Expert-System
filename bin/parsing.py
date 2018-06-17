import bin.shunting_yard as shunting_yard


class Fact(object):
    def __init__(self, name):
        self.name = name
        self.on = -1


class Rule(object):
    def __init__(self, ipn_condition, ipn_conclusion):
        self.ipn_condition = ipn_condition
        self.ipn_conclusion = ipn_conclusion
        self.used = 0


def find_fact(facts, letter):
    for i in facts:
        if i and i.name == letter:
            return i
    return None


def parse_ipn(facts, ipn):
    nbr_fact = 0
    nbr_ope = 0
    for word in ipn:
        for letter in word:
            if 'A' <= letter <= 'Z':
                fact = find_fact(facts, letter)
                if not fact:
                    fact = Fact(letter)
                    facts.append(fact)
                nbr_fact += 1
            elif letter in ['+', '|', '^']:
                nbr_ope += 1
    return facts, nbr_fact, nbr_ope


def update_lists(facts, rules, ipn_stat, ipn_conc):
    new_rule = Rule(ipn_stat, ipn_conc)
    rules.append(new_rule)
    facts, nbr_fact, nbr_ope = parse_ipn(facts, ipn_stat)
    if nbr_ope == nbr_fact - 1:
        facts, nbr_fact, nbr_ope = parse_ipn(facts, ipn_conc)
        if nbr_ope == nbr_fact - 1:
            return facts, rules
    return None, None


def get_condition(elements):
    idx_word, idx_letter, ipn_condition = shunting_yard.create_ipn(elements)
    del elements[0:idx_word]
    elements[0] = elements[0][idx_letter:]
    if elements[0][0] not in ['<', '=']:
        return None, None
    return elements, ipn_condition


def get_conclusion(elem, facts, rules, ipn_condition):
    condition = 0
    if elem[0][0:2] == '=>':
        condition = 2
    elif elem[0][0:3] == '<=>':
        condition = 3
    if len(elem[0]) > condition:
        elem[0] = elem[0][condition:]
    else:
        del elem[0]
    idx_word, idx_letter, ipn_conclusion = shunting_yard.create_ipn(elem)
    if len(elem) > idx_word and elem[idx_word][idx_letter] != '#':
        return None, None
    if condition == 3:
        facts, rules = update_lists(facts, rules, ipn_conclusion, ipn_condition)
    facts, rules = update_lists(facts, rules, ipn_condition, ipn_conclusion)
    return facts, rules


def get_queries_init(elements, facts):
    infos = []
    if len(elements[0]) == 1:
        del elements[0]
    else:
        elements[0] = elements[0][1:]
    print(elements)
    for word in elements:
        for letter in word:
            if 'A' <= letter <= 'z':
                fact = find_fact(facts, letter)
                if not fact:
                    return None
                infos.append(letter)
            elif letter == '#':
                return infos
            else:
                return None
    return infos
