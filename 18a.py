import sys

dirs = {'L': (0,-1), 'R': (0,1), 'D': (1,0), 'U': (-1,0)}

cur = [0,0]
coords = [cur]
perimeter = 0
for line in sys.stdin.readlines():
    dir, steps, color = line.strip().split()
    dir_coord = dirs[dir]
    move = [i*int(steps) for i in dir_coord]
    cur = [cur[i] + move[i] for i in range(2)]
    coords.append(cur)
    perimeter += int(steps)

print(coords)

#coords = [[0,0], [0,5], [5,5], [5,0], [0,0]]

xs = [loc[0] for loc in coords]
ys = [loc[1] for loc in coords]
print(xs, ys)

a1 = a2 = 0
for i in range(len(xs)-1):
    a1 += xs[i] * ys[i+1]
    a2 += ys[i] * xs[i+1]

print(a1, a2)
area = abs(a1 - a2)/2 + perimeter/2 + 1
print(area)
