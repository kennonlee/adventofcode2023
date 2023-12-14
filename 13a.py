import itertools, numpy, sys

def arr_tostring(pat):
    ret = ''
    for line in pat:
        ret += line + '\n'
    return ret

def score(pat):
    for y in range(len(pat) - 1):
        if pat[y] == pat[y+1]:
            # verify from reflection point outwards
            y1 = y-1
            y2 = y+2
            reflective = True
            while y1 >= 0 and y2 < len(pat):
                print("comparing", y1, y2, pat[y1], pat[y2])
                if pat[y1] != pat[y2]:
                    reflective = False
                    break
                y1 -= 1
                y2 += 1
            if reflective == True:
                print("reflective, index", y + 1)
                return y + 1
            else:
                print("not reflective, continuing")
    return 0

pat = []
total = 0
# added an extra newline to end of input to ensure the last pattern is handled
for line in sys.stdin.readlines():
#    print("line", line)
    if (s := line.strip()) != "":
        pat.append(s)
    else:
        # process the current pattern
        print(arr_tostring(pat))
        ret = 100 * score(pat)
        if ret == 0:
            print("none found, transposing")
            # transpose and try again
            trans = [''.join(s) for s in (zip(*pat))]
            print(arr_tostring(trans))
            ret = score(trans)
        total += ret
        pat.clear()

print(total)

