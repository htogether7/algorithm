import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
check = [[0] * n for _ in range(n)]
q = deque([])
q.append([0,0])
check[0][0] = 1

dp = [[-1] * n for _ in range(n)]
if board[0][0] == 0:
    dp[0][0] = 1

while q:
    r,c = q.popleft()
    if r + 1 < n:
        if check[r+1][c] == -1:
            q.append([r+1,c])
        if dp[r][c] != 0:
            if board[r][c] == 0:
                if board[r+1][c] == 1:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                    check[r+1][c] = 1
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
                    check[r+1][c] = 0
            elif board[r][c] == 1:
                if board[r+1][c] == 2:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                    check[r+1][c] = 1
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
                    check[r+1][c] = 0
            elif board[r][c] == 2:
                if board[r+1][c] == 0:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                    check[r+1][c] = 1
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
                    check[r+1][c] = 0
        else:
            if board[r+1][c] == 0:
                dp[r+1][c] = max(dp[r+1][c],1)
                check[r+1][c] = 1
#         if check[r+1][c] == 0:
#             check[r+1][c] = 1
#             q.append([r+1,c])

    if c + 1 < n:
        if check[r][c+1] == -1:
            q.append([r,c+1])
        if dp[r][c] != 0:
            if board[r][c] == 0:
                if board[r][c+1] == 1:
                    
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                    check[r][c+1] = 1
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
                    check[r][c+1] = 0
            elif board[r][c] == 1:
                if board[r][c+1] == 2:
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                    check[r][c+1] = 1
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
                    check[r][c+1] = 0
            elif board[r][c] == 2:
                if board[r][c+1] == 0:
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                    check[r][c+1] = 1
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
                    check[r][c+1] = 0
        else:
            if board[r][c+1] == 0:
                dp[r][c+1] = max(dp[r][c+1], 1)
                check[r][c+1] = 1
#         if check[r][c+1] == 0:
#             check[r][c+1] = 1
#             q.append([r,c+1])
print(dp)
print(dp[-1][-1])
# print(dp)
# print(q)
# print(board)
