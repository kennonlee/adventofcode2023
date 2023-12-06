import sys

def strings_to_ints(lst):
    ret = filter(lambda x: x.isdigit(), lst)
    ret = [int(i.strip()) for i in ret]
    return ret

ttime, threshold = ["".join(s.split(":")[1].strip().split()) for s in sys.stdin.readlines()]

winners = 0
for button_time in range(1, ttime):
    dist = button_time * (ttime - button_time)
    if dist > threshold:
        winners += 1

# quadratic - -x^2 + 40929790 - 215106415051100 > 0 
# 6192351 to 34737439 = 28545089