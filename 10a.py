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

print(steps)
    



              