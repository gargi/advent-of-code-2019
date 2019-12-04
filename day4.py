start = 240920
end = 789857
part_1 = 0
part_2 = 0

def check_consc(nums):
    for i in range(1, 6):
        if nums[i] < nums[i-1]:
            return False
    return True

def check_similar(nums):
    for i in range(1, 6):
        if nums[i] == nums[i-1]:
            return True
    return False

def check_two_adj(nums):
    curr = 1
    for i in range(1, 6):
        if nums[i] == nums[i-1]:
            curr += 1
        else:
            if curr == 2:
                return True
            curr = 1
    # Last consecutive digit check
    return curr == 2

for number in range(start, end+1):
    nums = [int(i) for i in str(number)]
    if check_consc(nums) and check_similar(nums):
        part_1 += 1
    if check_consc(nums) and check_two_adj(nums):
        part_2 += 1
print(part_1)
print(part_2)
