import sys
input = sys.stdin.readline

t = int(input())
result = []
for _ in range(t):
    k = int(input())
    files = list(map(int,input().split()))
    sum = [0]
    for file in files:
        sum.append(sum[-1] + file)
    dp = [[0] * k for _ in range(k)]
    # for i in range(k):
        # dp[i][i] = files[i]
    for i in range(k-1):
        # dp[i][i] = files[i]
        dp[i][i+1] = files[i] + files[i+1]
    
    for i in range(k-1, -1, -1):
        for j in range(i+2,k):
            for s in range(i, j):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i][s] + dp[s+1][j]
                else:
                    dp[i][j] = min(dp[i][j], dp[i][s] + dp[s+1][j])
            dp[i][j] += sum[j+1] - sum[i]
            
    # print(dp)
    result.append(dp[0][-1])


for r in result:
    print(r)