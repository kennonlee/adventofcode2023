import itertools, sys

def get_wilds(record):
    ret = []
    for x, c in enumerate(record):
        if c == '?':
            ret.append(x)
    return ret

def get_sets(record):
    sets = []
    count = 0
    in_set = False
    for x, c in enumerate(record):
        if c == '#':
            if not in_set:
                in_set = True
            count += 1
        else:
            if in_set: 
                in_set = False
                sets.append(count)
                count = 0
            # else do nothing
    if in_set:
        sets.append(count)
    return sets        

def is_valid(record, sets):
    if get_sets(record) == sets:
        return True
    else:
        return False
    
def get_permutations(record, sets):
    wilds = get_wilds(record)
    missing = sum(sets) - sum(get_sets(record)) 
    perms = itertools.combinations(wilds, missing)
    ret = 0
    for p in perms:
        test = record
        for x in p:
            test = test[:x] + '#' + test[x+1:]
            if is_valid(test, sets):
                ret += 1
#        print(test, sets, is_valid(test, sets))
    return ret

lines = []
for line in sys.stdin.readlines():
    record, sets = line.split()
    counts = [int(i) for i in sets.split(',')]
    lines.append((record, counts))

print(lines)
ret = 0
for line in lines:
    record, sets = line
#    print(get_wilds(record), get_sets(record), is_valid(record, sets))
    ret += get_permutations(record, sets)
print(ret)

