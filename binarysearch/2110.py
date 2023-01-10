import sys;

input = sys.stdin.readline;
n, c = map(int, input().split());

board = [int(input()) for _ in range(n)];

board.sort()

l = 0
r = board[-1]-1
answer =  0
while l <= r:
    mid = (l+r) // 2
    tmp_count = 1
    pos = board[0]
    for i in range(1, len(board)):
        if board[i] - pos >= mid:
            tmp_count += 1
            pos = board[i]
    if tmp_count < c:
        r = mid-1
    elif tmp_count >= c:
        l = mid+1
        answer = max(answer,mid)
    # print(mid, tmp_count, pos)
    # breakㅂ
print(answer)

# print(board)
# if c == 2:
    # print(board[-1] - board[0])
# else:
    
# print(board)
# start = board[0];
# end = board[-1];

# min_length = end-start;
# c -= 2;
# while c:
    # mid = (start + end) // 2;


# print(board);
