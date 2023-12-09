import sys

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

count = 0
cur = "AAA"
while True:
    for c in instr:
        count += 1
#        print(count, cur, nodes[cur], c)
        if c == 'L':
            cur = nodes[cur][0]
        else:
            cur = nodes[cur][1]
        if cur == 'ZZZ':
            print(count)
            exit()