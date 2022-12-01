import sys
from collections import deque
input = sys.stdin.readline
r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

# q = deque()
j_q = deque()
f_q = deque()
time = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == "J":
            j_q.append([i,j,0])
        if board[i][j] == "F":
            f_q.append([i,j,0])

dr = [1,-1,0,0]
dc = [0,0,1,-1]

possible = False
while j_q:
    prev_j = []
    prev_f = []


    if f_q and f_q[0][2] == time:
        prev_r, prev_c, prev_t = f_q.popleft()
        prev_f.append([prev_r, prev_c, prev_t])
        for i in range(4):
            if 0 <= prev_r + dr[i] < r and 0 <= prev_c + dc[i] < c and (board[prev_r+dr[i]][prev_c+dc[i]] == "." or board[prev_r+dr[i]][prev_c+dc[i]] == ","):
                f_q.append([prev_r+dr[i], prev_c+dc[i], time+1])
                board[prev_r+dr[i]][prev_c+dc[i]] = "F"
    else:
        if j_q and j_q[0][2] != time:
            time += 1
        prev_r, prev_c, prev_t = j_q.popleft()
        if prev_r == r-1 or prev_r == 0 or prev_c == c-1 or prev_c == 0:
            print(prev_t+1)
            possible = True
            break
        board[prev_r][prev_c] = ","
        prev_j.append([prev_r, prev_c, prev_t])
        for i in range(4):
            if 0 <= prev_r + dr[i] < r and 0 <= prev_c + dc[i] < c and board[prev_r+dr[i]][prev_c+dc[i]] == ".":
                j_q.append([prev_r+dr[i], prev_c+dc[i], time+1])
                board[prev_r+dr[i]][prev_c+dc[i]] = "J"
                if prev_r+dr[i] == r-1 or prev_r+dr[i] == 0 or prev_c+dc[i] == c-1 or prev_c+dc[i] == 0:
                    print(prev_t+2)
                    possible = True
                    break
    if possible:
        break
    # print(j_q,f_q,time)
    # print(board)

if not possible:
    print("IMPOSSIBLE")
    


# print(j_q, f_q)
