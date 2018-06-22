import sys


def check_contradiction(facts, graph, path, test):
    cpy = list(path)
    for fact in facts:
        if facts[fact]:
            if len(fact) == 1 and '!' + fact in facts and traversal('!' + fact, graph, facts, cpy, test):
                    if not test:
                        print('Contradiction in the fact', fact, 'has been found')
                        sys.exit(1)
                    else:
                        print('Contradiction in the fact', fact, 'may exist')
            elif len(fact) == 2 and fact[0] == '!' and fact[1:] in facts and traversal(fact[1:], graph, facts, cpy, test):
                    if not test:
                        print('Contradiction in the fact', fact[1], 'has been found')
                        sys.exit(1)
                    else:
                        print('Contradiction in the fact', fact, 'may exist')


def traversal(fact, graph, facts, path, test):
    if fact in path:
        return facts[fact]
    path.append(fact)
    if facts[fact]:
        return True
    for edge in graph[fact]:
        if edge[-1] == '+':
            if traversal(edge[0], graph, facts, path, test) and traversal(edge[1], graph, facts, path, test):
                facts[fact] = True
                if not test:
                    check_contradiction(facts, graph, path, test)
                return True
        elif edge[-1] == '|':
            if traversal(edge[0], graph, facts, path, test) or traversal(edge[1], graph, facts, path, test):
                facts[fact] = True
                if not test:
                    check_contradiction(facts, graph, path, test)
                return True
        elif edge[-1] == '^':
            if traversal(edge[0], graph, facts, path, test) ^ traversal(edge[1], graph, facts, path, test):
                facts[fact] = True
                if not test:
                    check_contradiction(facts, graph, path, test)
                return True
        elif edge[-1] == '!':
            if not traversal(edge[0], graph, facts, path, test):
                facts[fact] = True
                if not test:
                    check_contradiction(facts, graph, path, test)
                return True
        elif edge[-1] in facts:
            facts[fact] = traversal(edge[-1], graph, facts, path, test)
            if facts[fact] and not test:
                check_contradiction(facts, graph, path, test)
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


def initialise_test(facts):
    for test in facts:
        if 'A' <= test <= 'Z':
            facts[test] = True


def inference(facts, graph, queries, init):
    print('Checking for contradictions...')
    initialise_test(facts)
    path = []
    check_contradiction(facts, graph, path, True)
    for fact in queries:
        reinitialise(facts, init)
        path = []
        print('\nChecking for fact', fact, '...')
        state = traversal(fact, graph, facts, path, False)
        if state:
            print_path(facts, path, init)
        print('Fact', fact, 'is', state)

