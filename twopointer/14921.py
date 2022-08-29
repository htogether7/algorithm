import sys;
input = sys.stdin.readline;
n = int(input());

board = list(map(int, input().split()));

l = 0;
r = n-1;
result = board[l] + board[r];
while True:
    if abs(board[l+1] + board[r]) >= abs(board[l] + board[r-1]):
        r -= 1;
    else:
        l += 1;
    
    if l == r:
        break;
    if abs(result) > abs(board[l] + board[r]):
        result = board[l] + board[r];

print(result);