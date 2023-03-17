import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
answer = 0
check = [[0] * n for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def dfs(r,c):
    if check[r][c]:
        return check[r][c]
    
    check[r][c] = 1

    for i in range(4):
        next_r = r + dy[i]
        next_c = c + dx[i]
        if next_r < 0 or next_r >= n or next_c < 0 or next_c >= n:
            continue
        if board[r][c] >= board[next_r][next_c]:
            continue
        # if check[next_r][next_c] != 0:
        check[r][c] = max(check[r][c], dfs(next_r,next_c)+1)
        # else:
            # dfs(next_r,next_c,l+1)
    return check[r][c]

for row in range(n):
    for col in range(n):
        # if check[row][col] == 0:
            # check[row][col] = 1
        answer = max(answer,dfs(row,col))
print(answer)
# for row in range(n):
#     for col in range(n):
#         # if check[row][col] != 0:
#             # continue
#         q = deque([])
#         q.append((row,col,1))
#         while q:
#             r,c,count = q.popleft()
#             check[r][c] = count
#             for i in range(4):
#                 next_r = r + dy[i]
#                 next_c = c + dx[i]
#                 if next_r < 0 or next_r >= n or next_c < 0 or next_c >=n:
#                     continue
#                 if board[next_r][next_c] <= board[r][c]:
#                     continue
#                 if count+1 > check[next_r][next_c]:
#                     q.append((next_r,next_c,count+1))
# print(check)






# print(board)