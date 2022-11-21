import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]
# print(board)
# print(dp)

q = deque([[0,0]])
if board[0][0] == 0:
    dp[0][0][0] = 1
# print(dp)
while q:
    r,c = q.popleft()
    if 0 <= r+1 < n:
        if dp[r+1][c] == [0,0,0]:
            q.append([r+1,c])
        if dp[r][c] == [0,0,0]:
            if board[r+1][c] == 0:
                dp[r+1][c][0] = max(dp[r+1][c][0], 1)
        else:
            for i in range(3):
                dp[r+1][c][i] = max(dp[r][c][i], dp[r+1][c][i])
            if dp[r][c][(board[r+1][c]-1)%3] != 0:
                dp[r+1][c][board[r+1][c]] = max(dp[r+1][c][board[r+1][c]], dp[r][c][(board[r+1][c]-1)%3] + 1)
    if 0 <= c+1 < n:
        if dp[r][c+1] == [0,0,0]:
            q.append([r,c+1])
        if dp[r][c] == [0,0,0]:
            if board[r][c+1] == 0:
                dp[r][c+1][0] = max(dp[r][c+1][0], 1)
        else:
            for i in range(3):
                dp[r][c+1][i] = max(dp[r][c][i], dp[r][c+1][i])
            if dp[r][c][(board[r][c+1]-1)%3] != 0:
                dp[r][c+1][board[r][c+1]] = max(dp[r][c+1][board[r][c+1]], dp[r][c][(board[r][c+1]-1)%3] + 1)

print(max(dp[-1][-1]))