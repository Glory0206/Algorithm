import sys

N = int(sys.stdin.readline())

total = 0

for k in range(1, N):
    total += k * (N + 1)

print(total)