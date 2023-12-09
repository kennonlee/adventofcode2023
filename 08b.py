import sys

# brute force algo below. Ended up just checking if LCM for the 6 paths
# was the answer, and it was.
#
# ['BFA', 'AAA', 'DFA', 'XFA', 'QJA', 'SBA']
# 14257 11567 16409 21251 18023 19637
# LCM = 14,449,445,933,179
# https://www.calculatorsoup.com/calculators/math/lcm.php

nodes = {}

instr = sys.stdin.readline().strip()
print(instr)

# skip the blank line
sys.stdin.readline()

for line in sys.stdin.readlines():
    name, lr = [i.strip() for i in line.split("=")]
    left, right = lr.split(",")
    left = left.strip()[1:]
    right = right.strip()[:-1]
    nodes[name] = (left, right)
#    print(name, left, right)

curs = []
for name in nodes.keys():
    if name[2] == 'A':
        curs.append(name)
print(curs)

count = 0
while True:
    for c in instr:
        zcount = 0
        count += 1
        if count % 10000000 == 0:
            print(count)
#        print(count, cur, nodes[cur], c)
        for i, cur in enumerate(curs):
            if c == 'L':
                curs[i] = nodes[curs[i]][0]
            else:
                curs[i] = nodes[curs[i]][1]
        for name in curs:
            if name[2] == 'Z':
                zcount += 1
                print(count, zcount, curs)
        if zcount > 2:
            print(count, zcount, curs)
        if zcount == len(curs):
            print(count)
            exit()