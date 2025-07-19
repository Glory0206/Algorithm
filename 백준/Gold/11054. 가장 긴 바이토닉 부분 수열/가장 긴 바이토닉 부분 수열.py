l = int(input())

nums = list(map(int, input().split()))
reversed_nums = list(reversed(nums))

left_to_right = [1] * l
right_to_left = [1] * l
for i in range(l):
    for j in range(i):
        if nums[j] < nums[i]:
            left_to_right[i] = max(left_to_right[i], left_to_right[j] + 1)
        if reversed_nums[j] < reversed_nums[i]:
            right_to_left[i] = max(right_to_left[i], right_to_left[j] + 1)

max_len = 0
for i in range(l):
    max_len = max(max_len, left_to_right[i] + right_to_left[l - i - 1])

print(max_len - 1)