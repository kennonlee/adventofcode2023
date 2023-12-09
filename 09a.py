import itertools, sys

def strings_to_ints(lst):
    ret = [int(i.strip()) for i in lst]
    return ret

def all_zeroes(lst):
    return all([i == 0 for i in lst])        

sum = 0
for line in sys.stdin.readlines():
    cur = strings_to_ints(line.split())
 #   print(vals)
    arrs = [cur]
    while not all_zeroes(cur):
        arr = []
        for x, y in itertools.pairwise(cur):
            arr.append(y-x)
        cur = arr
        arrs.append(cur)
#    print(arrs)

    arrs.reverse()
    for lower, upper in itertools.pairwise(arrs):
        if all_zeroes(lower):
            lower.append(0)
        upper.append(upper[-1] + lower[-1])
    print(arrs, arrs[-1][-1])
    sum += arrs[-1][-1]

print(sum)
