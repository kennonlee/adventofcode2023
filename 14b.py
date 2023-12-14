import datetime, sys

def roll(highest, y, x):
    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
    newloc = highest[x]
#    print("rolling", x, "from", y, "to", newloc)
    lines[newloc] = lines[newloc][:x] + 'O' + lines[newloc][x+1:]

lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

def spin(lines):
    # stores most northward loc to move a stone to
    highest = [0] * len(lines[0])
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                highest[x] = min(highest[x], y)
            elif c == '#':
                highest[x] = y+1
            else:
                # roll!
                if highest[x] < y:
                    roll(highest, y, x)
                    highest[x] = highest[x] + 1
                else:
                    highest[x] = y + 1

def rotate(arr):
    return [''.join(reversed(s)) for s in (zip(*arr))]

def printlines(lines):
    for line in lines:
        print(line)
    print("")

states = [lines.copy()]
found = False
for i in range(1000000000):
    if found == True:
        break
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)
    for x, state in enumerate(states):
        if state == lines:
            print("cycle found! ", x, i)
            found = True
            break
    states.append(lines.copy())

remainder = (1000000000 - x) % (i - x)
for i in range(remainder):
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)
    spin(lines)
    lines = rotate(lines)

lines.reverse()
score = 0
for y, line in enumerate(lines):
    score += (y+1) * line.count('O')

print(score)


