import math

N = input()

nums = [0] * 10

for n in N:
    if n == '6' or n == '9':
        nums[6] += 0.5
    else:
        nums[int(n)] += 1

print(math.ceil(max(nums)))