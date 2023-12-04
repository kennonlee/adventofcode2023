import sys

color_max = {"red": 12, "green": 13, "blue": 14}

def is_valid(vals):
    for sets in vals.split(";"):
         for draw in sets.split(","):
#            print(draw)
            xxx, count, color = draw.split(" ")
            if not is_valid_count(color.strip(), int(count)):
                 return False
    return True 
         
def is_valid_count(color, count):
     return color_max[color] >= count

total = 0
for line in sys.stdin.readlines():
    game, vals = line.split(":")
    gamenum = int(game.split(" ")[1])
    if is_valid(vals):
            print(True, vals)
            total += gamenum

print(total)
