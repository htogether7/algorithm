import sys;
from collections import deque;
n = int(input());
board = [list(map(int, input())) for _ in range(n)];

check = [[0] * n for _ in range(n)];

counts = [];

dx = [1,-1,0,0];
dy = [0,0,1,-1];

for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            q = deque([]);
            count = 0;
            q.append([r,c]);
            board[r][c] = 0;
            while q:
                row,col = q.popleft();
                
                count += 1;
                for i in range(4):
                    if 0<=row+dy[i] < n and 0<=col+dx[i] < n:
                        if board[row+dy[i]][col+dx[i]] == 1:
                            q.append([row+dy[i], col+dx[i]]);
                            board[row+dy[i]][col+dx[i]] = 0;
            counts.append(count);
counts.sort();

print(len(counts));
for i in counts:
    print(i);
# print(board);

