import sys
input = sys.stdin.readline

n,k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

INF = 1000001
dp = [INF] * (k+1)

# for coin in coins:
    # dp[coin] = 1
dp[0] = 0

for ind in range(0, k+1):
    for coin in coins:
        if ind+coin >= k+1:
            continue
        dp[ind+coin] = min(dp[ind+coin], dp[ind] + 1)
if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])
# print(coins)

