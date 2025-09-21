num = input()

prev = num[0]
zero_groups = 1 if prev == '0' else 0
one_groups = 1 if prev == '1' else 0

for n in num[1:]:
    if n != prev:
        if n == '0':
            zero_groups += 1
        else:
            one_groups += 1
        prev = n

print(min(zero_groups, one_groups))