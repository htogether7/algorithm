import sys;
from collections import deque;
input = sys.stdin.readline;

m,n = map(int, input().split());
board = [];

for i in range(n):
    board.append(list(map(int, input().split())));

# checked = [[0]*m for _ in range(n)];
q = deque([]);
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append([i,j]);
            # checked[i][j] = 1;
# print(q);
# print(board);
dx = [0,0,-1,1];
dy = [1,-1,0,0];

# print(q);
while q:
    i,j= q.popleft();
    # checked[i][j] = 1;
    # time_max = max(time_max, count);

    for ind in range(4):
        if i+dy[ind] >= 0 and i+dy[ind] < n and j+dx[ind] >= 0 and j+dx[ind] < m:
            if board[i+dy[ind]][j+dx[ind]] == 0:
                q.append([i+dy[ind], j+dx[ind]]);
                board[i+dy[ind]][j+dx[ind]] = board[i][j] + 1;
    # print(q);
# print(board);

non_visit = False;
# time_max = 0;
time_max = 0;
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            non_visit = True;
            break;
        else:
            time_max = max(time_max, board[i][j])
    if non_visit:
        break;

# print(board);
if non_visit:
    print(-1);
else:
    print(time_max-1);