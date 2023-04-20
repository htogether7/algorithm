import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n)

for i in range(n):
    tmp = list(map(int,input().split()))
    time = tmp[0]
    pre = []
    if tmp[1] > 0:
        pre = tmp[2:]

    if not pre:
        dp[i] = time
    else:
        pre_max = 0
        for p in pre:
            pre_max = max(pre_max,dp[p-1])
        dp[i] = pre_max + time

print(max(dp))