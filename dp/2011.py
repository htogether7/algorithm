import sys
input = sys.stdin.readline
num = list(input().rstrip())

dp = [[0] * (len(num)+1) for _ in range(2)]
for i in range(1,(len(num)+1)):

    if num[i-1] != "0":
        dp[0][i] = dp[0][i-1]
        if i == 1:
            dp[0][i] = 1
        else:
            dp[0][i] += dp[1][i-2]

    else:
        dp[0][i] = 0

    
    if i < len(num) and 1<=int("".join(num[i-1:i+1]))<=26 and num[i-1] != "0":
        dp[1][i] = dp[0][i-1]
        if i == 1:
            dp[1][i] = 1
        else:
            dp[1][i] += dp[1][i-2]
    else:
        dp[1][i] = 0

print((dp[0][-1] + dp[1][-2]) % 1000000)