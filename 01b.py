import sys

def run():
    sum = 0
    for line in sys.stdin.readlines():
        sum += getval(line)
    print(sum)

nums = ["1","2","3","4","5","6","7","8","9",
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def convert(str):
    if str.isdigit():
        return int(str)
    match str:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9

def getval(line):
    first_index = 10000
    first_val = None
    last_index = -1
    last_val = None
    for num in nums:
        found = line.find(num)
        if found != -1 and found < first_index:
            first_index = found
            first_val = convert(num)
        rfound = line.rfind(num)
        if rfound != -1 and rfound > last_index:
            last_index = rfound
            last_val = convert(num)
            
    print(line, first_val, last_val)
    return first_val * 10 + last_val
        
run()
        
