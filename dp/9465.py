import sys;
input = sys.stdin.readline;

t = int(input());

for _ in range(t):
    n = int(input());
    board = [list(map(int,input().split())) for _ in range(2)];
    # print(board);
    dp = [0] * n * 2;

    for i in range(n*2):
        if i // 2 == 0:
            dp[i] = board[i][0];
        else:
            if i % 2 == 0:
                # 윗줄일때
                if i+2 < 2*n:
                    if board[0][i//2] + board[1][(i//2)+1] >= board[0][(i//2)+1]:
                        dp[i] = max(dp[i],dp[i-1] + board[0][i//2]);
                    else:
                        dp[i] = max(dp[i], dp[i-1] + board[0][(i//2)]);
                        dp[i+2] = max(dp[i+2], dp[i-1] + board[0][(i//2)+1]);
                else:
                    dp[i] = max(dp[i],dp[i-1] + board[0][i//2]);
            else:
                # 아랫줄일때
                if i+2 < 2*n:
                    if board[1][i//2] + board[0][(i//2)+1] >= board[1][(i//2)+1]:
                        dp[i] = max(dp[i],dp[i-3] + board[1][i//2]);
                    else:
                        dp[i] = max(dp[i], dp[i-3] + board[1][(i//2)]);
                        dp[i+2] = max(dp[i+2],dp[i-3] + board[1][(i//2)+1]);
                else:
                    dp[i] = max(dp[i],dp[i-3] + board[1][i//2]);
        # print(dp);
    print(max(dp[-1], dp[-2]));
    # dp[0] = board[0][0];
    # dp[1] = board[1][0];