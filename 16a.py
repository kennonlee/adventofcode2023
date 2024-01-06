import sys

beams = [((0,-1), (0,1))]
energized = dict()

def energize(start, dir):
    if (start, dir) in energized.keys():
        return

    energized[(start, dir)] = True

    y, x = [start[i] + dir[i] for i in range(len(start))] 
    if y < 0 or y >= len(tiles):
        return
    if x < 0 or x >= len(tiles[0]):
        return
    next_char = tiles[y][x]
#    print(start, dir, next_char)
    if next_char == '.':
        beams.append(((y, x), dir))
    elif next_char == '/':
        beams.append(((y, x), (-dir[1], -dir[0])))
    elif next_char == '\\':
        beams.append(((y, x), (dir[1], dir[0])))
    elif next_char == '-':
        if abs(dir[0]) == 1:
            beams.append(((y,x), (0,1)))
            beams.append(((y,x), (0,-1)))
        else:
            beams.append(((y,x), dir))
    elif next_char == '|':
        if abs(dir[1]) == 1:
            beams.append(((y,x), (1,0)))
            beams.append(((y,x), (-1,0)))
        else:
            beams.append(((y,x), dir))

tiles = []
for line in sys.stdin.readlines():
    tiles.append(line.strip())

energized = dict()

while(len(beams) > 0):
    start, dir = beams.pop()
    energize(start, dir)

final = dict()
for i in energized.keys():
    final[i[0]] = True

def printall():
    drawn = tiles.copy()
    for coord, dir in energized.keys():
        y, x = coord
        if drawn[y][x] == '.':
            drawn[y] = drawn[y][:x] + '*' + drawn[y][x+1:]

    for d in drawn:
        print(d)

printall()
# minus one for the starting coord
print(len(final) - 1)



