from collections import Counter

name = input().strip()
counter = Counter(name)

odd_count = sum(1 for c in counter if counter[c] % 2 == 1)

if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    half = []
    middle = ""

    for c in sorted(counter.keys()):
        if counter[c] % 2 == 1:
            middle = c
        half.append(c * (counter[c] // 2))

    left = "".join(half)
    right = left[::-1]
    print(left + middle + right)