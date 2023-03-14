import sys
n = int(input())

sizes = []

for _ in range(n):
    r, c = map(int, input().split())
    sizes.append([r,c])

def solution(n):
    dp = [[0] * n for _ in range(n)]
    num = [[0] * n for _ in range(n)]
    for i in range(n):
        num[i][i] = sizes[i][0] * sizes[i][1]

    for plus in range(1, n):
        for row in range(0, n-plus):
            if plus == 1:
                dp[row][row+plus] = sizes[row][0] * sizes[row][1] * sizes[row+1][1]
                
            else:
                for m in range(row, row+plus):
                    tmp_sum = dp[row][m] + dp[m+1][row+plus] + num[row][m] * sizes[row+plus][1]
                    if dp[row][row+plus] == 0:
                        dp[row][row+plus] = tmp_sum
                    else:
                        dp[row][row+plus] = min(dp[row][row+plus], tmp_sum)
                        
            num[row][row+plus] = sizes[row][0] *  sizes[row+plus][1]
    return dp[0][-1]

answer = solution(n)

print(answer)