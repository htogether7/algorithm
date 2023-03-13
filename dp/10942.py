import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int,input().split()))
m = int(input())
result = []

dp = [[1] * n for _ in range(n)]


def fill_dp(n):
    for plus in range(n):
        for r in range(n-plus):
            if plus == 0:
                dp[r][r+plus] = 1
            else:
                if board[r] != board[r+plus]:
                    dp[r][r+plus] = 0
                else:
                    dp[r][r+plus] = dp[r+1][r+plus-1]

fill_dp(n)

for _ in range(m):
    s,e = map(int, input().split())
    result.append(dp[s-1][e-1])


for r in result:
    print(r)