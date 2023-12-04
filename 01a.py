import sys

def run():
    sum = 0
    for line in sys.stdin.readlines():
        sum += getval(line)
    print(sum)

def getval(line):
    first = None
    last = None
    for c in line:
        if c.isdigit():
            if first is None:
                first = int(c)
            last = int(c)
    print(line, first, last)
    return first * 10 + last
        
run()
        
