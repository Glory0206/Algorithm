from itertools import combinations

n = int(input())

nums = sorted(list(map(int, input().split())))

count = 0

for i in range(n):
    target = nums[i]

    start, end = 0, n-1

    while start < end:
        current_sum = nums[start] + nums[end]

        if current_sum == target:
            if start != i and end != i:
                count += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif current_sum < target:
            start += 1
        else:
            end -= 1
print(count)