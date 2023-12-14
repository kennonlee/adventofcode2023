import sys

pipe_dirs = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((-1, 0), (0, 1)),
    "J": ((-1, 0), (0, -1)),
    "7": ((1, 0), (0, -1)),
    "F": ((1, 0), (0, 1))
}

def add_tup(t1, t2):
    return tuple(map(lambda i, j: i+j, t1, t2))


def valid_dirs(arr, loc, dir):
    cur_pipe = arr[loc[0]][loc[1]]
    print(cur_pipe, dir)
    if cur_pipe not in pipe_dirs: 
        return False
    dirs = pipe_dirs[cur_pipe]
    return dir in dirs

arr = []
start = None
for line in sys.stdin.readlines():
    sx = line.find("S")
    if sx != -1:
        start = (len(arr), sx) 
    arr.append(line.strip())
print(start)

path = dict()
path[start] = True

locs = []
prior_dirs = []
for dir in ((-1,0), (1,0), (0,-1), (0,1)):
    loc = add_tup(start, dir)
    inverse = tuple(map(lambda i: -1*i, dir))
    print("testing", loc)
    if valid_dirs(arr, loc, inverse):
        locs.append(loc)
        prior_dirs.append(inverse)

print(locs, prior_dirs)

steps = 1
while (locs[0] != locs[1]):
    path[locs[0]] = True
    path[locs[1]] = True
#    print(locs, prior_dirs, steps)
    # do both directions
    for i in range (0, 2):
        loc = locs[i]
#        print("loc", loc)
        pipe = arr[loc[0]][loc[1]]
        dirs = pipe_dirs[pipe]
        for dir in dirs:
            if dir != prior_dirs[i]:
                prior_dirs[i] = tuple(map(lambda i: -1*i, dir))
#                print(pipe, loc, dir)
                locs[i] = add_tup(locs[i], dir) 
                break
    steps += 1

path[locs[0]] = True

print(steps)
print(len(path))

inside = 0
for y in range(len(arr)):
    verts = 0
    last_vert = None
    for x in range(len(arr[0])):
        if (y,x) in path:
            p = arr[y][x]
            if p == '|' or (p == 'J' and last_vert == 'F') or (p == '7' and last_vert == 'L'):
                verts += 1
            if p in ('J', 'F', '|', '7', 'L'):
                last_vert = p
        if (y,x) not in path:
            if verts % 2 == 1:
                arr[y] = arr[y][:x] + str(verts%10) + arr[y][x+1:]
                inside += 1
            else:
                arr[y] = arr[y][:x] + '~' + arr[y][x+1:]
            
for line in arr:
    print(line)

print(inside)

              