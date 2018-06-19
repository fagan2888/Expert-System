import sys
import bin.parsing as parsing
import bin.graph_manager as graph_manager


def open_file(argv):
    try:
        assert len(argv) == 2
        file_name = argv[1]
        fd = open(file_name, "r")
    except AssertionError:
        print("Expert system takes one argument only")
        sys.exit(1)
    except FileNotFoundError:
        print("This file does not exist")
        sys.exit(1)
    except IsADirectoryError:
        print("The argument is a directory")
        sys.exit(1)
    return fd


def check_errors(facts, queries, init):
    if not facts:
        print('No rule has been given')
        sys.exit(1)
    if not queries:
        print('No queries have been given')
        sys.exit(1)
    if not init:
        print('No initial statement has been given')
        sys.exit(1)


def fill_graph(facts, graph):
    for fact in facts:
        if fact not in graph:
            graph[fact] = []


def fill_facts(facts, graph):
    for node in graph:
        if node not in facts and node != 'count':
            facts[node] = False


def parse_file(fd):
    facts = {}
    graph = {}
    queries = []
    init = []
    graph['count'] = 0
    with fd:
        for line_nb, line in enumerate(fd):
            elements = line.split()
            if elements and elements[0][0] == '?':
                if not facts:
                    check_errors(facts, queries, init)
                queries = parsing.get_queries_init(elements, facts)
            elif elements and elements[0][0] == '=':
                if not facts:
                    check_errors(facts, queries, init)
                init = parsing.get_queries_init(elements, facts)
            elif elements and elements[0][0] != '#':
                if queries or init:
                    print('File must end with queries and an initial statement (line %d)' % line_nb)
                    sys.exit(1)
                elements, ipn_condition = parsing.get_condition(elements)
                if not ipn_condition:
                    print('Syntax error at line %d : %s' % (line_nb, line))
                    sys.exit(1)
                if not graph_manager.update_graph(elements, facts, graph, ipn_condition):
                    print('Syntax error at line %d : %s' % (line_nb, line))
                    sys.exit(1)
    check_errors(facts, queries, init)
    fill_graph(facts, graph)
    fill_facts(facts, graph)
    return facts, graph, queries, init
