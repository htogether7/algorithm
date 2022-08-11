import sys;
input = sys.stdin.readline;
n,m = map(int, input().split());

# 1x4 1가지
# 2x2 1가지
# 2x3 3가지
# 3x2 3가지
# 4x1 1가지

block_sizes = [[1,4], [2,2], [2,3], [3,2], [4,1]];

board = [list(map(int,input().split())) for _ in range(n)];
result = 0;
for (i,[dy,dx]) in enumerate(block_sizes):
    # print(y,x);
    if i == 0:
        for y in range(0,n-dy+1):
            for x in range(0, m-dx+1):
                result = max(result, sum(board[y][x:x+dx]));
    elif i == 1:
        for y in range(0, n-dy+1):
            for x in range(0, m-dx+1):
                tmp = board[y][x] + board[y][x+1] + board[y+1][x] + board[y+1][x+1];
            
                result = max(result, tmp);

    elif i == 2:
        for y in range(0, n-dy+1):
            for x in range(0, m-dx+1):
                result = max(result, sum(board[y][x:x+dx]) + board[y+1][x]);
                result = max(result, sum(board[y][x:x+dx]) + board[y+1][x+1]);
                result = max(result, sum(board[y][x:x+dx]) + board[y+1][x+2]);
                result = max(result, sum(board[y+1][x:x+dx]) + board[y][x]);
                result = max(result, sum(board[y+1][x:x+dx]) + board[y][x+1]);
                result = max(result, sum(board[y+1][x:x+dx]) + board[y][x+2]);
                result = max(result, sum(board[y][x+1:x+dx]) + sum(board[y+1][x:x+2]));
                result = max(result, sum(board[y][x:x+2]) + sum(board[y+1][x+1:x+dx]));

    elif i == 3:
        for y in range(0,n-dy+1):
            for x in range(0, m-dx+1):  
                tmp = board[y][x] + board[y+1][x] + board[y+2][x];
                result = max(result, tmp + board[y][x+1]);
                result = max(result, tmp + board[y+1][x+1]);
                result = max(result, tmp + board[y+2][x+1]);
                tmp = board[y][x+1] + board[y+1][x+1] + board[y+2][x+1];
                result = max(result, tmp + board[y][x]);
                result = max(result, tmp + board[y+1][x]);
                result = max(result, tmp +  board[y+2][x]);
                result = max(result, board[y][x] + board[y+2][x+1] + sum(board[y+1][x:x+dx]))
                result = max(result, board[y+2][x] +  board[y][x+1] + sum(board[y+1][x:x+dx]))

    elif i == 4:
        for y in range(0,n-dy+1):
            for x in range(0, m-dx+1):  
                tmp = board[y][x]+board[y+1][x]+board[y+2][x] +board[y+3][x]
                result = max(result, tmp);
print(result);