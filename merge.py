def merge_list(a,b):
    if any(type(x) is not int for x in a + b):
        raise TypeError("inputs must be int")
    a.sort()
    b.sort()
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out
