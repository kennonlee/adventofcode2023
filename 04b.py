import numpy, sys

def strings_to_ints(lst):
    # strip out non-numeric oddities like empty strings; might not be necessary
    ret = filter(lambda x: x.isdigit(), lst)
    ret = [int(i.strip()) for i in ret]
    return ret

lines = []
for line in sys.stdin.readlines():
    lines.append(line)

card_counts = numpy.ones(len(lines))

for i in range(len(lines)):
    line = lines[i]
    card, data = line.strip().split(":")
    winners, owned = [i.strip() for i in data.split("|")]
    winners = strings_to_ints(winners.split())
    owned = strings_to_ints(owned.split())
    match = list(set(winners) & set(owned))
    for j in range(len(match)):
        card_counts[i+j+1] += card_counts[i]
    # debug testing
    if i < 5:
        print(len(match))
        print(card_counts)

print(sum(card_counts))
