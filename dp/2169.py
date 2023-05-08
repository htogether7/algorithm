import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dp = [list(map(int,input().split())) for _ in range(n)]

for c in range(1,m):
    dp[0][c] += dp[0][c-1]

for r in range(1, n):
    lr = dp[r][::]
    rl = dp[r][::]

    for c in range(m):
        if c == 0:
            lr[c] += dp[r-1][c]
        else:
            lr[c] += max(dp[r-1][c], lr[c-1])
    
    for c in range(m-1,-1,-1):
        if c == m-1:
            rl[c] += dp[r-1][c]
        else:
            rl[c] += max(dp[r-1][c], rl[c+1])
    
    for c in range(m):
        dp[r][c] = max(lr[c], rl[c])

print(dp[-1][-1])