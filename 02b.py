import sys

def power_set(vals):
    maxes = {"red": 0, "green": 0, "blue": 0}
    for sets in vals.split(";"):
        for draw in sets.split(","):
            xxx, count, color = [i.strip() for i in draw.split(" ")]
            count = int(count)
            if maxes[color] < count:
                 maxes[color] = count
    return maxes["red"] * maxes["green"] * maxes["blue"]
         
total = 0
for line in sys.stdin.readlines():
    game, vals = line.split(":")
    total += power_set(vals)

print(total)
