import bin.shunting_yard as shunting_yard
import bin.parsing as parsing
import bin.graph_operators as g_oper
import sys


def get_nodes(ipn):
    if len(ipn) == 1:
        return ipn[0]
    facts = []
    while len(ipn) > 1:
        for idx, elem in enumerate(ipn):
            if elem == '+':
                g_oper.addition(ipn, idx, facts)
                break
            elif elem == '!':
                g_oper.negation(ipn, idx, facts)
                break
            elif elem in ['|', '^']:
                print('Operator \'|\' and \'^\' is not supported in conclusions')
                sys.exit(1)
    cpy = []
    for fact in facts:
        while fact[:2] == '!!':
            fact = fact[2:]
        cpy.append(fact)
    return cpy


def add_nodes(graph, nodes, rule):
    for node in nodes:
        if node in graph:
            graph[node].append(rule)
        else:
            graph[node] = [rule]


def manage_rule(graph, ipn, nodes):
    while len(ipn) > 3:
        for idx, elem in enumerate(ipn):
            if elem in ['+', '|', '^']:
                graph[str(graph['count'])] = [ipn[idx - 2: idx + 1]]
                ipn[idx] = str(graph['count'])
                ipn.pop(idx - 1)
                ipn.pop(idx - 2)
                graph['count'] = graph['count'] + 1
                break
            elif elem == '!':
                graph[str(graph['count'])] = [[ipn[idx - 1], '!']]
                ipn[idx] = str(graph['count'])
                ipn.pop(idx - 1)
                graph['count'] = graph['count'] + 1
                break
    add_nodes(graph, nodes, ipn)


def add_edges(graph, ipn_stat, nodes):
    if len(ipn_stat) <= 3:
        add_nodes(graph, nodes, ipn_stat)
    else:
        manage_rule(graph, ipn_stat, nodes)


def check_errors(facts, ipn_stat, ipn_conc):
    facts, nbr_fact, nbr_ope = parsing.parse_ipn(facts, ipn_stat)
    if nbr_ope == nbr_fact - 1:
        facts, nbr_fact, nbr_ope = parsing.parse_ipn(facts, ipn_conc)
        if nbr_ope == nbr_fact - 1:
            return True
    return False


def update_edges(facts, graph, ipn_stat, ipn_conc):
    if not check_errors(facts, ipn_stat, ipn_conc):
        return False
    nodes = get_nodes(ipn_conc)
    add_edges(graph, ipn_stat, nodes)
    return True


def update_graph(elem, facts, graph, ipn_condition):
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
    if not ipn_conclusion:
        return False
    if len(elem) > idx_word and elem[idx_word][idx_letter] != '#':
        return False
    if condition == 3 and not update_edges(facts, graph, ipn_conclusion.copy(), ipn_condition.copy()):
        return False
    return update_edges(facts, graph, ipn_condition, ipn_conclusion)
