import sys

nums = list(map(int, input().split()))
sorted_nums = sorted(nums)

al_nums = {
    'A': sorted_nums[0],
    'B': sorted_nums[1],
    'C': sorted_nums[2]
}

seq = input()

print(' '.join(str(al_nums[ch]) for ch in seq))