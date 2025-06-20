n, m, k = map(int, input().split())

teams = min(n // 2, m)

while n+m - teams * 3 < k:
    teams -= 1

print(teams)