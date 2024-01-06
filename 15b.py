import sys

def hash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def remove(box, name):
    for i, lens in enumerate(box):
        if lens[0] == name:
            box = box[:i] + box[i+1:]
            print("removed from box:", box, name)
            return box
    # name not found
    print("not found in box:", box, name)
    return box

def add(box, name, foc):
    for lens in box:
        if lens[0] == name:
            lens[1] = foc
            return
    # lens not found
    print("added to box:", box, name, foc)
    box.append([name, foc])

steps = sys.stdin.readline().strip().split(',')

boxes = []
for i in range(256):
    boxes.append([])

for step in steps:
    cmd = None
    if '-' in step:
        name = step[:-1]
        box = hash(name)
        boxes[box] = remove(boxes[box], name)
    else:
        name, foc = step.split('=')
        box = hash(name)
        foc = int(foc)
        print("box:", box, name, foc)
        add(boxes[box], name, foc)

    for i, box in enumerate(boxes):
        if len(box) > 0:
            print(i, box)


for i, box in enumerate(boxes):
    if len(box) > 0:
        print(i, box)

ret = 0
for i, box in enumerate(boxes):
    for x, lens in enumerate(box):
        val = (i+1) * (x+1) * lens[1] 
        print(val)
        ret += val

print(ret)
