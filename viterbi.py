def order(num, x):
    from collections import defaultdict
    dict = defaultdict(list)
    for i, j in x:
        dict[j].append(i)

    def _order(key): #recursively sort the values at a given key
        for keys in dict[key]:
            if dict.get(keys, "") != "": #does the child exist as another key? If yes:
                if dict[keys] != []: #has the child key been seen? If yes:
                    yield from _order(keys) #call sort with the child key and yield the deeper recursive calls.
                    dict[keys] = [] #now that the child key has been seen.
            else: yield keys #the child does not exist as another key, so:yield that value. it is a starting node.
        if dict[key] != []: #after the recursion if the parent key has not been seen:
            yield key #yield the parent key it is the next in order value
            dict[key] = [] #the parent key has been seen.

    ordered = []

    for a in dict:
        ordered += list(_order(a))
    return ordered[:num]

def longest(num, x):
    ord_lst = order(num, x)
    long = []
    long2 = []
    for a in ord_lst:
        for i in x[a]:
            long.append(i)
    print(long)
