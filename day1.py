import math
total = 0
def part_1(num):
    return math.ceil(int(num)/3) - 2


def part_2(num):
    curr_mass = 0
    while num > 0:
        curr = math.ceil(int(num)/3) - 2
        if curr <= 0: return curr_mass
        curr_mass += curr
        num = curr
    return curr_mass

f = open("day1_input.txt")
input = list(line.strip() for line in f)
for num in input:
    total += part_2(num)
print(total)
