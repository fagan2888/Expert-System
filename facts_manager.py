import sys

class Fact(object):
    def __init__(self, name, ipn):
        self.name = name
        self.on = False
        self.ipn = [ipn]


def find_fact(facts, letter):
    for i in facts:
        if i and i.name == letter:
            return i
    return None


def find_operator(ipn_conc):
    if not ipn_conc:
        return None
    for idx, i in enumerate(ipn_conc):
        if i in ['+', '|', '!']:
            return idx
    return None


def complex_conclusion(facts, ipn_stat, ipn_con, idx_ope):
    while idx_ope:
        if ipn_con[idx_ope] == '+' and idx_ope > 1:
            
        if len(ipn_conc) >= idx_ope:
            idx_ope = find_operator(ipn_conc[idx_ope:])

def create_fact(facts, ipn_stat, ipn_conc):
    idx_ope = find_operator(ipn_conc)
    if idx_ope:
        complex_conclusion(facts, ipn_stat, ipn_conc, idx_ope)
    else:
        if len(ipn_conc) != 1:
            return None
    print(ipn_stat)
    print(ipn_conc)

