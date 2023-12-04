import sys

def strings_to_ints(lst):
    ret = filter(lambda x: x.isdigit(), lst)
    ret = [int(i.strip()) for i in ret]
    return ret

score = 0
for line in sys.stdin.readlines():
    xx, data = line.strip().split(":")
    winners, owned = [i.strip() for i in data.split("|")]
    winners = strings_to_ints(winners.split(" "))
    owned = strings_to_ints(owned.split(" "))
    match = list(set(winners) & set(owned))
    print(winners, "|", owned, "|", match)
    if len(match) > 0:
        score += 2 ** (len(match) - 1)

print(score)
