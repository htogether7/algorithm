import sys;
input = sys.stdin.readline;
r,c,n = map(int,(input().split()));

board = [list(input().rstrip()) for _ in range(r)]

for row in range(r):
    for col in range(c):
        if board[row][col] == "O":
            board[row][col] = 0;
time = 0;

dx = [1,-1,0,0];
dy = [0,0,1,-1];

while time < n:
    if time == 0:
        for row in range(r):
            for col in range(c):
                if board[row][col] == ".":
                    board[row][col] = 0;
                else:
                    board[row][col] += 1;
    else:
        for row in range(r):
            for col in range(c):
                board[row][col] += 1;
        for row in range(r):
            for col in range(c):
                if board[row][col] == 3:
                    board[row][col] = 0;
                    for i in range(4):
                        if 0<=row+dy[i]<r and 0<=col+dx[i]<c:
                            # print(row+dy[i],col+dx[i]);
                            if dy[i] == 0 and dx[i] == 1:
                                if board[row+dy[i]][col+dx[i]] == 3:
                                    # print(row,col);
                                    continue;
                            if dy[i] == 1 and dx[i] == 0:
                                if board[row+dy[i]][col+dx[i]] == 3:
                                    continue;
                            board[row+dy[i]][col+dx[i]] = 0;


    time += 1;
# print(board[1][3] == "0")
# print(board);
for row in range(r):
    for col in range(c):
        if board[row][col] == 0:
            board[row][col] = ".";
        else:
            board[row][col] = "O"

for row in range(r):
    board[row] = "".join(board[row]);
for _ in range(r):
    print(board[_]);
# print(r,c,n);
