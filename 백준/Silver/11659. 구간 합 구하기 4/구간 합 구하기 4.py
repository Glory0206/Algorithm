import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (N+1)
for i in range(1, N+1):
    prefix_sum[i] = prefix_sum[i-1] + num_list[i-1]

for _ in range(M):
    f, l = map(int, sys.stdin.readline().split())
    print(prefix_sum[l] - prefix_sum[f-1])