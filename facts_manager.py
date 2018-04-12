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


def get_priority(elements, idx_word, idx_letter, priority):
    """

    :rtype: returns a value according to the operators in conclusion
    Nothing:            1
    Nothing and '!':    0
    '+':                1
    '+' and '!':        0
    '|':                3
    '|' and '!'         2
    """
    if len(elements[idx_word]) >= idx_letter:
        if elements[idx_word][idx_letter + 1] == '+':
            return priority
        elif elements[idx_word][idx_letter + 1] == '|':
            return priority + 2
        elif elements[idx_word][idx_letter + 1] != '#':
            print('False operator in the conclusion at line %d' % line_nb)
            sys.exit(1)
    elif
        
            
        
        len(elements) >= idx_word:
        

def create_fact(facts, elements, ipn, line_nb):
    priority = 1
    for idx_word, word in enumerate(elements):
        for idx_letter, letter in enumerate(word):
            if letter == '!'
                priority = 0
            if 'A' <= letter <= 'Z':
                priority = get_priority(elements, idx_word, idx_letter, priority)
                if not facts:
                    facts.append(Fact(letter, ipn))
                else:
                    new = find_fact(facts, letter)
                    if not new:
                        facts.append(Fact(letter, ipn))
                    else:
                        new.ipn.append(ipn)
            elif letter == '#':
                return facts
            elif letter != '+' and letter != '|' and letter != '!':
                print('False operator in the conclusion at line %d' % line_nb)
                sys.exit(1)
    return facts


