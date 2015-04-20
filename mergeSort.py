def merge(l1, l2):
    res = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            res.append(l1[i])
            i += 1
        else:
            res.append(l2[j])
            j += 1
    if i != len(l1):
        res.extend(l1[i:])
    else:
        res.extend(l2[j:])
    return res

def merge_sort(L):
    print L
    if len(L) == 1:
        return L
    else:
        middle = len(L)/2
        return merge(merge_sort(L[:middle]), merge_sort(L[middle:]))
