def addition(ipn, idx, facts, buf):
    if ipn[idx - 2]:
        facts.append(ipn[idx - 2])
        buf.append(ipn[idx - 2])
    if ipn[idx - 1]:
        facts.append(ipn[idx - 1])
        buf.append(ipn[idx - 1])
    ipn[idx] = False
    ipn.pop(idx - 1)
    ipn.pop(idx - 2)


def negation(ipn, idx, facts, buf):
    if not ipn[idx - 1]:
        while buf:
            ret = buf.pop()
            facts.append('!' + ret)
            if ret in facts:
                facts.remove(ret)
    elif ipn[idx - 1]:
        facts.append('!' + ipn[idx - 1])
        buf.append('!' + ipn[idx - 1])
    ipn[idx] = False
    ipn.pop(idx - 1)
