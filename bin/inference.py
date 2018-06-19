import sys


def check_contradiction(facts, graph, path):
    cpy = list(path)
    for fact in facts:
        if facts[fact]:
            if len(fact) == 1 and '!' + fact in facts and traversal('!' + fact, graph, facts, cpy):
                    print('Contradiction in the fact', fact, 'has been found')
                    sys.exit(1)
            elif len(fact) == 2 and fact[0] == '!' and fact[1:] in facts and traversal(fact[1:], graph, facts, cpy):
                    print('Contradiction in the fact', fact[1], 'has been found')
                    sys.exit(1)


def traversal(fact, graph, facts, path):
    if fact in path:
        return facts[fact]
    path.append(fact)
    if facts[fact]:
        return True
    for edge in graph[fact]:
        if edge[-1] == '+':
            if traversal(edge[0], graph, facts, path) and traversal(edge[1], graph, facts, path):
                facts[fact] = True
                check_contradiction(facts, graph, path)
                return True
        elif edge[-1] == '|':
            if traversal(edge[0], graph, facts, path) or traversal(edge[1], graph, facts, path):
                facts[fact] = True
                check_contradiction(facts, graph, path)
                return True
        elif edge[-1] == '^':
            if traversal(edge[0], graph, facts, path) ^ traversal(edge[1], graph, facts, path):
                facts[fact] = True
                check_contradiction(facts, graph, path)
                return True
        elif edge[-1] == '!':
            if not traversal(edge[0], graph, facts, path):
                facts[fact] = True
                check_contradiction(facts, graph, path)
                return True
        elif edge[-1] in facts:
            facts[fact] = traversal(edge[-1], graph, facts, path)
            if facts[fact]:
                check_contradiction(facts, graph, path)
            return facts[edge[-1]]
    return False


def reinitialise(facts, init):
    for fact in facts:
        if fact in init:
            facts[fact] = True
        else:
            facts[fact] = False


def print_path(facts, path, init):
    print('Path: ', end='', flush=True)
    first = True
    for i in reversed(path):
        if 'A' <= i <= 'Z' and facts[i] and i in init:
            if first:
                print(i, end='', flush=True)
                first = False
            else:
                print(' --', i, end='', flush=True)
        elif 'A' <= i <= 'Z' and facts[i]:
            if first:
                print(i, end='', flush=True)
                first = False
            else:
                print(' -->', i, end='', flush=True)
    print('\n', end='', flush=True)


def inference(facts, graph, queries, init):
    for fact in queries:
        reinitialise(facts, init)
        path = []
        print('Checking for fact', fact, '...')
        state = traversal(fact, graph, facts, path)
        if state:
            print_path(facts, path, init)
        print('Fact', fact, 'is', state, '\n\n')
