import sys

def strings_to_ints(lst):
    ret = filter(lambda x: x.isdigit(), lst)
    ret = [int(i.strip()) for i in ret]
    return ret

times, distances = [strings_to_ints(s.split(":")[1].strip().split()) for s in sys.stdin.readlines()]
races = list(zip(times, distances))

ret = 1
for race in races:
    ttime, threshold = race
    winners = []
    for button_time in range(1, ttime):
        dist = button_time * (ttime - button_time)
        if dist > threshold:
            winners.append(button_time)
    print(winners)
    ret *= len(winners)

print(ret)
