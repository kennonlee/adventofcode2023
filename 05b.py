import sys

# reverse brute force, starting with end location 0 and incrementing
# up until we find a location that maps to a valid seed value

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

def priorval(val, map):
    for line in map:
#        print(line)
        dest, src, rng = line
        if val >= dest and val < dest + rng:
            return src + val - dest
    return val

seed_ranges = []
for start, len in zip(seeds[0::2], seeds[1::2]):
    seed_ranges.append((start, len))
print(seed_ranges)

# swap the map order since we are going backwards
maps.reverse()
end = 0
while True:
    ret = end
    vals = [end]
    for map in maps:
        ret = priorval(ret, map)        
        vals.append(ret)
    for seed_range in seed_ranges:
        start, len = seed_range
        if ret >= start and ret < start + len:
            print("WOOHOO!", seed_range, ret, end, vals)
            exit()
#    print(vals)
    if end % 1000000 == 0:
        vals.reverse()
        print(ret, vals, end)
    end += 1

