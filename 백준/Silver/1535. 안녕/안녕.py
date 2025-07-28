N = int(input())

minus = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [0] * 101

for i in range(N):
    for hp in range(99, minus[i] - 1, -1):
        dp[hp] = max(dp[hp], dp[hp - minus[i]] + happy[i])

print(max(dp[1:]))