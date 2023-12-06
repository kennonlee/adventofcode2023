import sys

maps = [[], [], [], [], [], [], []]

def strings_to_ints(lst):
    ret = filter(lambda x: x.isdigit(), lst)
    ret = [int(i.strip()) for i in ret]
    return ret

map_index = -1
for line in sys.stdin.readlines():
    tokens = line.split(":")
    if tokens[0] == "seeds":
        seeds = strings_to_ints(tokens[1].strip().split())
    # found a map title
    elif "map:" in line:
            map_index += 1
    else:
        vals = line.strip().split()
        if len(vals) == 3:
            vals = strings_to_ints(vals)
            maps[map_index].append(vals)

print(seeds)
print(maps)

def nextval(val, map):
    for line in map:
#        print(line)
        dest, src, rng = line
        if val >= src and val <= src + rng:
            return dest + val - src 
    return val

locs = []
for seed in seeds:
    ret = seed
    for map in maps:      
        ret = nextval(ret, map)
#        print(seed, ret, map)
    locs.append(ret)

print(locs, min(locs))
