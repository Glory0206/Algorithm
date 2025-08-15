l, r = input().split()
count = 0

if len(l) != len(r):
    print(0)
else:
    for a, b in zip(l, r):
        if a != b:
            break
        if a == '8':
            count += 1

    print(count)