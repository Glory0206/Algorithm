N, b = map(int, input().split())

bit = 0

for i in range(b+1):
    bit += 2**i

print("yes" if N <= bit else "no")