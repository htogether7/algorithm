import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [list(input().rstrip()) for _ in range(n)]
check_normal = [[0] * n for _ in range(n)]
check_rg = [[0] * n for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
# print(check_normal)
# 일반인
normal_count = 0
for i in range(n):
    for j in range(n):
        if check_normal[i][j] == 0:
            check_normal[i][j] = 1
            normal_count += 1
            q = deque([])
            q.append([i,j])
            tmp = board[i][j]
            while q:
                next_y, next_x = q.popleft()
                for k in range(4):
                    if 0 <= next_y + dy[k] < n and 0 <= next_x + dx[k] < n and board[next_y+dy[k]][next_x+dx[k]] == tmp:
                        if check_normal[next_y + dy[k]][next_x + dx[k]] == 0:
                            q.append([next_y + dy[k], next_x + dx[k]])
                            check_normal[next_y + dy[k]][next_x + dx[k]] = 1
            # print(check_normal)

# print(check_normal)
# print(normal_count)
# 적록색약
rg_count = 0
for i in range(n):
    for j in range(n):
        if check_rg[i][j] == 0:
            check_rg[i][j] = 1
            rg_count += 1
            q = deque([])
            q.append([i,j])
            tmp = board[i][j]
            while q:
                next_y, next_x = q.popleft()
                for k in range(4):
                    if 0 <= next_y + dy[k] < n and 0 <= next_x + dx[k] < n:
                        if board[next_y+dy[k]][next_x+dx[k]] == tmp or (tmp=="R" and board[next_y+dy[k]][next_x+dx[k]] == "G") or (tmp=="G" and board[next_y+dy[k]][next_x+dx[k]] == "R"):
                            if check_rg[next_y + dy[k]][next_x + dx[k]] == 0:
                                q.append([next_y + dy[k], next_x + dx[k]])
                                check_rg[next_y + dy[k]][next_x + dx[k]] = 1
            # print(check_rg)
# print(check_rg)
# print(rg_count)
# # print(check_normal)
print(normal_count, rg_count)

