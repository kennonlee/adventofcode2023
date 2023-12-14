import itertools, sys

def dist(g1, g2):
    y1, x1 = g1
    y2, x2 = g2

    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    ret = x2 - x1 + y2 - y1
    extra = 0
    for i in range(x1, x2):
        if blankx[i]:
#            print("x", i)
            extra += 1
    for i in range(y1, y2):
        if blanky[i]:
#            print("y", i)
            extra += 1
    ret += extra
#    print (g1, g2, extra, ret)
    return ret

img = []
gals = []
for line in sys.stdin.readlines():
    img.append(line.strip())

# find blank lines and cols, and galaxies
blanky = dict.fromkeys([i for i in range(len(img))], False)
blankx = dict.fromkeys([i for i in range(len(img[0]))], True)
for y, line in enumerate(img):
    if all(map(lambda c: c == '.', line)):
        blanky[y] = True

    for x in range(len(line)):
        if line[x] == '#':
            blankx[x] = False
            gals.append((y,x))

print(blanky)
print(blankx)
print(gals)

sum = 0
pairs = 0
for x, g1 in enumerate(gals):
    for g2 in gals[x+1:]:
        pairs += 1
        sum += dist(g1, g2)

print(pairs, sum)



