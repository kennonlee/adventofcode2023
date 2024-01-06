import sys

dirs = ((0,1),(0,-1),(1,0),(-1,0))

def slocs(garden, start):
    ret = set()
    for dir in dirs:
        cur = (start[0] + dir[0], start[1] + dir[1])
        if cur[0] not in range(len(garden)) or cur[1] not in range(len(garden[0])):
            continue
        if garden[cur[0]][cur[1]] != '#':
            ret.add(cur)
    return ret

def locs(garden, starts, steps):
    ret = set()
    if steps == 1:
        for start in starts:
            ret.update(slocs(garden, start))
    else:
        new_starts = set()
        for start in starts:
            new_starts.update(slocs(garden, start))
        ret.update(locs(garden, new_starts, steps - 1))
    return ret

garden = []
for line in sys.stdin.readlines():
    line = line.strip()
    garden.append(line)

start = None
for y, row in enumerate(garden):
    for x, c in enumerate(row):
        if c == 'S':
            start = [(y, x)]

possible = locs(garden, start, 64) 
print(len(possible), possible)


