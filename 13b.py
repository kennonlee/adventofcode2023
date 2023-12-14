import sys

def arr_tostring(pat):
    ret = ''
    for line in pat:
        ret += line + '\n'
    return ret

def score(pat, orig):
#    print(arr_tostring(pat))
    for y in range(len(pat) - 1):
#        print("checking", y, pat[y], pat[y+1])
        if pat[y] == pat[y+1] and y != orig-1:
            # verify from reflection point outwards
            y1 = y-1
            y2 = y+2
            reflective = True
            while y1 >= 0 and y2 < len(pat):
#                print("comparing", y1, y2, pat[y1], pat[y2])
                if pat[y1] != pat[y2]:
                    reflective = False
                    break
                y1 -= 1
                y2 += 1
            if reflective == True:
#                print("reflective, index", y + 1, orig)
                return y + 1
#            else:
#                print("not reflective, continuing")
    return 0

def smudge(p, orig):
    for y in range(len(p)):
        for x in range(len(p[0])):
            if p[y][x] == '.':
                oppo = '#'
            else:
                oppo = '.'
            edited = p.copy()
            edited[y] = edited[y][:x] + oppo + edited[y][x+1:]

            ret = 100 * score(edited, int(orig/100) if orig >= 100 else -1)

            if ret == 0:
                trans = [''.join(s) for s in (zip(*edited))]
                ret = score(trans, orig)
            if ret != 0:
                if ret == orig:
                    print("uhoh!!", orig, ret, "y", y, "x", x)
                    print(arr_tostring(p))
                    exit()
                print(arr_tostring(p))
                print("smudge y", y, "x", x, "score", ret)
                return ret

base = []
total = 0
# added an extra newline to end of input to ensure the last pattern is handled
for line in sys.stdin.readlines():
    if (s := line.strip()) != "":
        base.append(s)
    else:
        # process the current pattern
        orig = 100 * score(base, -1)
        if orig == 0:
            # transpose and try again
            trans = [''.join(s) for s in (zip(*base.copy()))]
            orig = score(trans, -1)

        total += smudge(base, orig)
        base.clear()

print(total)

