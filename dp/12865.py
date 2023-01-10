import sys;
input = sys.stdin.readline;

n,k = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())));
board.append([1,0])
board.sort(key = lambda x : x[0]);
# print(board);

dp = [[0] * (k+1) for _ in range(n+1)]
# print(dp)
# tmp_max = 0
# for ind in range(k+1):
    # for w,v in board:
# for c in range(1, k+1):
    # for r in range(1, n+1):
        # dp[r][c] = max(dp[r][c-1], )
        # if r == 1:
            # f
#         # print(w,v);
#         if ind + w < k+1:
#             dp[ind+w] = max(dp[ind+w], dp[ind] + v);
#             # tmp_max = max(tmp_max,dp[ind+w])
#             # dp[ind+w] = max(dp[ind+w], tmp_max)
            
#     # print(dp, ind)
# # print(max(dp));
# print(dp[-1]);
# print(dp)
for r in range(n+1):
    for c in range(1,k+1):
        if c - board[r][0] >= 0:
            dp[r][c] = max(dp[r-1][c], dp[r-1][c-board[r][0]] + board[r][1])
        else:
            dp[r][c] = dp[r-1][c]
print(dp[-1][-1])
        # dp[r][c] = max(dp[r-1][c])