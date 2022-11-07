import sys;
input = sys.stdin.readline;

n,k = map(int, input().split())

board = []

for _ in range(n):
    board.append(list(map(int,input().split())));

board.sort(key = lambda x : x[0]);
# print(board);

dp = [0] * (k+1)
for ind in range(k+1):
    for w,v in board:
        # print(w,v);
        if ind + w < k+1:
            dp[ind+w] = max(dp[ind+w], dp[ind] + v);

# print(max(dp));
print(dp[-1]);
# print(dp)