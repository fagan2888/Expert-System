def addition(ipn, idx, facts):
    if ipn[idx - 2]:
        facts.append(ipn[idx - 2])
    if ipn[idx - 1]:
        facts.append(ipn[idx - 1])
    ipn[idx] = False
    ipn.pop(idx - 1)
    ipn.pop(idx - 2)


def negation(ipn, idx, facts):
    if ipn[idx - 1]:
        facts.append('!' + ipn[idx - 1])
    else:
        cpy = []
        for fact in facts:
            cpy.append('!' + fact)
        facts = cpy
    ipn[idx] = False
    ipn.pop(idx - 1)