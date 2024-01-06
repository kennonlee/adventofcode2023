import sys

steps = sys.stdin.readline().strip().split(',')

ret = 0
for step in steps:
    val = 0
    for c in step:
        val += ord(c)
        val *= 17
        val %= 256
    print(step, val)
    ret += val

print(ret)
