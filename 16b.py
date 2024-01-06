import sys

def energize(beams, energized, start, dir):
    # seen this before, skip it
    if (start, dir) in energized.keys():
        return
    # add to seen list
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


def run(start, dir):
    energized = dict()
    beams = [(start, dir)]
    while(len(beams) > 0):
        start, dir = beams.pop()
        energize(beams, energized, start, dir)

    final = dict()
    for i in energized.keys():
        final[i[0]] = True
    return len(final) - 1

def test_all():
    top = 0

    for y in range(len(tiles)):
        top = max(top, run((y, -1), (0,1)))
        top = max(top, run((y, len(tiles[0])), (0,-1)))

    for x in range(len(tiles[0])):
        top = max(top, run((-1, x), (1, 0)))
        top = max(top, run((len(tiles), x), (-1, 0)))

    return top
print(test_all())

def printall():
    drawn = tiles.copy()
    for coord, dir in energized.keys():
        y, x = coord
        if drawn[y][x] == '.':
            drawn[y] = drawn[y][:x] + '*' + drawn[y][x+1:]

    for d in drawn:
        print(d)


