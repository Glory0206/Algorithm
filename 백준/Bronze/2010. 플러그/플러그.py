import sys

total = 0

multi = int(sys.stdin.readline())
for _ in range(multi):
    total += int(sys.stdin.readline())

print(total - multi + 1)