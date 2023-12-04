import sys

class PartNum:
    def __init__(self, y, x1, x2, val):
        self.y = y
        self.x1 = x1  
        self.x2 = x2
        self.val = val

    def info(self, arr):
#        return f"{self.y} {self.x1} {self.x2} {self.val} {self.get_adjacents()}, {self.is_adjacent(arr)}"
        return f"{self.y} {self.x1} {self.x2} {self.val} {self.is_adjacent(arr)}"

    # find all coordinates for points adjacent to this partnum
    def get_adjacents(self):
        ret = []
        for x in range(self.x1-1, self.x2+2):
            ret.append((self.y-1, x))
            ret.append((self.y+1, x))
        ret.append((self.y, self.x1-1))
        ret.append((self.y, self.x2+1))
        return ret

    # check if there is a part adjacent to this partnum
    def is_adjacent(self, arr):
        ymax = len(arr)
        xmax = len(arr[0])
        adjacents = self.get_adjacents()
        for a in adjacents:
            if a[0] >= 0 and a[0] < ymax and a[1] >= 0 and a[1] < xmax:
                c = arr[a[0]][a[1]]
                if not c.isdigit() and c != '.':
                    return True
        return False

partnums = []

arr = []
for line in sys.stdin.readlines():
    arr.append(line.strip())

in_num = False
for y in range(len(arr)):
    line = arr[y]
    start = -1
    end = -1        

    in_num = False
    for x in range(len(line)):
        c = line[x]
        if c.isdigit(): 
            if not in_num:
                in_num = True
                start = x
            end = x
            # edge case for line ending with a part number
            if end == len(line) - 1:
                print(y, start, end, line[start:end+1])
                partnums.append(PartNum(y, start, end, int(line[start:end+1])))
        else:
            if in_num:
                print(y, start, end, line[start:end+1])
                partnums.append(PartNum(y, start, end, int(line[start:end+1])))
                in_num = False
                start = -1
                end = -1


sum = 0
for partnum in partnums:
    if partnum.is_adjacent(arr):
        sum += partnum.val

print(sum)

#print([i.info(arr) for i in partnums])
