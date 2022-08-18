import sys;

input = sys.stdin.readline;
n, c = map(int, input().split());

board = [int(input()) for _ in range(n)];

board.sort();

start = board[0];
end = board[-1];

min_length = end-start;
c -= 2;
while c:
    mid = (start + end) // 2;


print(board);
