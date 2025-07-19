n = int(input())
stair = [0]
dp = [0] * (n+1)

for _ in range(n):
    stair.append(int(input()))

dp[1] = stair[1]

if n >= 2:
    dp[2] = stair[1] + stair[2]

# dp[i] =  stairs[i] + dp[i-2]: 마지막 계단 + 마지막에서 2칸 떨어져있는 계단까지의 값
# dp[i] = stair[i] + stair[i-1] + dp[i - 3]: 마지막 계단 + 마지막 1칸 전 계단 + 1칸전의 계단에서 2칸 떨어져있는 계단까지의 값
for i in range(3, n+1):
    dp[i] = max(dp[i - 2], dp[i - 3] + stair[i - 1]) + stair[i]

print(dp[n])