import sys

def roll(y, x):
    lines[y] = lines[y][:x] + '.' + lines[y][x+1:]
    newloc = highest[x]
#    print("rolling", x, "from", y, "to", newloc)
    lines[newloc] = lines[newloc][:x] + 'O' + lines[newloc][x+1:]

lines = []
for line in sys.stdin.readlines():
    lines.append(line.strip())

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
                roll(y, x)
                highest[x] = highest[x] + 1
            else:
                highest[x] = y + 1

lines.reverse()
score = 0
for y, line in enumerate(lines):
    score += (y+1) * line.count('O')

print(score)


