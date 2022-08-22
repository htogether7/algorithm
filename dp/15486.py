import sys;

input = sys.stdin.readline;

n = int(input());

arr = [list(map(int, input().split()))for _ in range(n)];

board = [0] * (n+1);

# max_price = 0;
for (ind,x) in enumerate(arr):
    time = x[0];
    price = x[1];
    if ind + time <= n:
        board[ind+time] = max(board[ind+time], board[ind] + price);
    if ind + 1 <= n:
        board[ind+1] = max(board[ind+1], board[ind]);
        # if board[ind] == 0:
        #     board[ind+time] = max(board[ind+time], max(board[ind-2:ind+1])+price);
        # else:
        #     if board[ind+time] < board[ind] + price:
        #         board[ind + time] = board[ind] + price;
                # print(board[ind+time]);
                # for i in range(ind,ind+time):
                    # board[i] = max(board[i], board[ind])
                # max_price = max_price + price;
                # print(max_price);
print(board);
print(max(board));
# print(board[-1]);

# print(arr);