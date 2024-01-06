import sys

dirs = {'2': (0,-1), '0': (0,1), '1': (1,0), '3': (-1,0)}

cur = [0,0]
coords = [cur]
perimeter = 0
for line in sys.stdin.readlines():
    _, __, encoded = line.strip().split()
    encoded = encoded[2:-1]
    dir_coord = dirs[encoded[-1]]
    steps = eval('0x' + encoded[:-1])
    move = [i*int(steps) for i in dir_coord]
    cur = [cur[i] + move[i] for i in range(2)]
    coords.append(cur)
    perimeter += int(steps)

#print(coords)

xs = [loc[0] for loc in coords]
ys = [loc[1] for loc in coords]
#print(xs, ys)

a1 = a2 = 0
for i in range(len(xs)-1):
    a1 += xs[i] * ys[i+1]
    a2 += ys[i] * xs[i+1]

#print(a1, a2)
area = abs(a1 - a2)/2 + perimeter/2 + 1
print(int(area))
