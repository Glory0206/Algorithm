N, M = map(int, input().split())
sets = float("inf")
one = float("inf")

for _ in range(M):
    s, o = map(int, input().split())
    sets = min(sets, s)
    one = min(one, o)

cost1 = ((N // 6) + 1) * sets

cost2 = (N // 6) * sets + (N % 6) * one

cost3 = N * one

print(min(cost1, cost2, cost3))