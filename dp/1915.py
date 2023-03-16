import sys
input = sys.stdin.readline
n,m = map(int,input().split())

board = [list(map(int,list(input().rstrip()))) for _ in range(n)]

dp = [[0 for _ in range(m)] for _ in range(n)]

answer = 0

for r in range(n):
    for c in range(m):
        if board[r][c] == 0:
            continue
        if r == 0 or c == 0:
            dp[r][c] = 1
            answer = max(answer , dp[r][c])
            continue
        dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
        answer = max(answer , dp[r][c])

print(answer ** 2)