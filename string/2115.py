import sys;
input = sys.stdin.readline;

n,m = map(int, input().split());

board = [list(input().rstrip())for _ in range(n)];

result = 0;

row = 1;
col = 1;

while row <= n-2:
    status = "none";
    while col <= m-2:
        # print(row,col,status);
        if board[row][col] == "." and board[row][col+1] == ".":
            if status == "none":
                if board[row-1][col] == "X" and board[row-1][col+1] == "X":
                    if board[row+1][col] == "X" and board[row+1][col+1] == "X":
                        # print("none", row, col)
                        col += 2;
                        status = "none";
                        result += 2;
                    else:
                        # print("up", row, col)
                        col += 1;
                        status = "up";
                        result += 1;
                elif board[row+1][col] == "X" and board[row+1][col+1] == "X":
                    # print("down", row, col)
                    col += 1;
                    status = "down";
                    result += 1;
                else:
                    # print("none", row,col);
                    col += 1;
                    status="none";
            elif status == "up":
                if board[row+1][col] == "X" and board[row+1][col+1] == "X":
                    # print("down", row, col)
                    col += 1;
                    status = "down";
                    result += 1;
                else:
                    # print("none", row, col);
                    col += 1;
                    status = "none";
            elif status == "down":
                if board[row-1][col] == "X" and board[row-1][col+1] == "X":
                    # print("up", row, col)
                    col += 1;
                    status = "up"
                    result += 1;
                else:
                    # print("none", row, col);
                    col += 1;
                    status = "none";
        else:
            # print("none", row,col)
            col += 1;
            status = "none";
    row += 1;
    col = 1;
        

row = 1;
col = 1;

while col <= m-2:
    status = "none";
    while row <= n-2:
        # print(row,col,status);
        if board[row][col] == "." and board[row+1][col] == ".":
            if status == "none":
                if board[row][col-1] == "X" and board[row+1][col-1] == "X":
                    if board[row][col+1] == "X" and board[row+1][col+1] == "X":
                        # print("none", row, col)
                        row += 2;
                        status = "none";
                        result += 2;
                    else:
                        # print("left", row, col)
                        row += 1;
                        status = "left";
                        result += 1;
                elif board[row][col+1] == "X" and board[row+1][col+1] == "X":
                    # print("right", row, col)
                    row += 1;
                    status = "right";
                    result += 1;
                else:
                    # print("none", row,col);
                    row += 1;
                    status="none";
            elif status == "left":
                if board[row][col+1] == "X" and board[row+1][col+1] == "X":
                    # print("right", row, col)
                    row += 1;
                    status = "right";
                    result += 1;
                else:
                    # print("none", row, col);
                    row += 1;
                    status = "none";
            elif status == "right":
                if board[row][col-1] == "X" and board[row+1][col-1] == "X":
                    # print("left", row, col)
                    row += 1;
                    status = "left"
                    result += 1;
                else:
                    # print("none", row, col);
                    row += 1;
                    status = "none";
        else:
            # print("none", row,col)
            row += 1;
            status = "none";
    col += 1;
    row = 1;

print(result);

# print(board);