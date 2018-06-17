import sys
import bin.parsing as parsing
import inference

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
    return fd


def print_all(facts, rules, queries, init):
    for i in facts:
        print(i.name)
    for j in rules:
        print(j.ipn_condition)
        print(j.ipn_conclusion)
    print(queries)
    print(init)


def parse_file(fd):
    facts = []
    rules = []
    queries = []
    init = []
    with fd:
        for line_nb, line in enumerate(fd):
            elements = line.split()
            if elements and elements[0][0] == '?':
                queries = get_queries_init(elements, facts)
                if not queries:
                    print('queryError: Fact does not exist or syntax error at line %d' % line_nb)
            elif elements and elements[0][0] == '=':
                init = get_queries_init(elements, facts)
                if not init:
                    print('initialStatementError: Fact does not exist or syntax error at line %d' % line_nb)
            elif elements and elements[0][0] != '#':
                if queries or init:
                    print('File must end with queries and an initial statement (line %d)' % line_nb)
                    sys.exit(1)
                elements, ipn_condition = parsing.get_condition(elements)
                if not ipn_condition:
                    print('Syntax error at line %d "%s"' % (line_nb, line))
                    sys.exit(1)
                facts, rules = parsing.get_conclusion(elements, facts, rules, ipn_condition)
                if not facts:
                    print('Syntax error at line %d "%s"' % (line_nb, line))
                    sys.exit(1)
    return facts, rules, queries, init



def start():
    fd = open_file(sys.argv)
    facts, rules, queries, init = parsing.parse_file(fd)
    inference.inference(facts, rules, queries, init)
    #print_all(facts, rules, queries, init)



if __name__ == "__main__":
    start()
