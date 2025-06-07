import sys
A, B = sys.stdin.readline().split()

sum_A = sum(map(int, A))
sum_B = sum(map(int, B))

print(sum_A * sum_B)