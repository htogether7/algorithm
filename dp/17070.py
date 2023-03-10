import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0,0,0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1


for row in range(n):
    for col in range(n):
        if row == 0 and col in [0,1]:
            continue

        dy = [0,-1,-1]
        dx = [-1,-1,0]
        for i in range(3):
            prev_row = row + dy[i]
            prev_col = col + dx[i]
            if prev_row < 0 or prev_col < 0:
                continue
            if board[row][col] == 1:
                continue

            if i == 0: # 왼쪽을 체크할 때는 이전에 왼쪽과 왼쪽 위에서 온 것만 더한다
                dp[row][col][i] = dp[prev_row][prev_col][0] + dp[prev_row][prev_col][1]
            elif i == 1: # 왼쪽 위를 체크할 때는 어디서 오든지 상관 없다
                if board[row-1][col] == 1 or board[row][col-1] == 1:
                    continue
                dp[row][col][i] = sum(dp[prev_row][prev_col])
            elif i == 2: # 위를 체크할 때는 이전에 왼쪽 위와 위에서 온 것만 더한다
                dp[row][col][i] = dp[prev_row][prev_col][1] + dp[prev_row][prev_col][2]
                
print(sum(dp[-1][-1]))
        




