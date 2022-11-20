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

dp = [[0] * n for _ in range(n)]
# print(check)
if board[0][0] != 0:
    starts = []
    while q:
        r,c = q.popleft()
        if r + 1 < n and check[r+1][c] == 0:
            check[r+1][c] = 1
            if board[r+1][c] == 0:
                starts.append((r+1,c))
            else:
                q.append([r+1,c])
        
        if c + 1 < n and check[r][c+1] == 0:
            check[r][c+1] = 1
            if board[r][c+1] == 0:
                starts.append((r,c+1))
            else:
                q.append([r,c+1])
    if not starts:
        print(0)
    else:
        pass
    print(starts)
    print(dp)
else:
    dp[0][0] = 1
    while q:
        r,c = q.popleft()
        if r + 1 < n:
            if board[r][c] == 0:
                if board[r+1][c] == 1:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
            elif board[r][c] == 1:
                if board[r+1][c] == 2:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
            elif board[r][c] == 2:
                if board[r+1][c] == 0:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c]+1)
                else:
                    dp[r+1][c] = max(dp[r+1][c], dp[r][c])
            if check[r+1][c] == 0:
                check[r+1][c] = 1
                q.append([r+1,c])

        if c + 1 < n:
            if board[r][c] == 0:
                if board[r][c+1] == 1:
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
            elif board[r][c] == 1:
                if board[r][c+1] == 2:
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
            elif board[r][c] == 2:
                if board[r][c+1] == 0:
                    dp[r][c+1] = max(dp[r][c]+1, dp[r][c+1])
                else:
                    dp[r][c+1] = max(dp[r][c], dp[r][c+1])
            if check[r][c+1] == 0:
                check[r][c+1] = 1
                q.append([r,c+1])
    print(dp[-1][-1])

# print(q)
# print(board)
