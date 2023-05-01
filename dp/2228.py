import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = [[[float('-inf')] * n for _ in range(n)] for _ in range(m)]

sums = []
for i in range(n):
    if i == 0:
        sums.append(int(input()))
    else:
        sums.append(sums[-1] + int(input()))

for i in range(m):
    for j in range(2*i,n):
        if i == 0:
            for k in range(j,n):
                if j == 0:
                    board[i][j][k] = sums[k]
                else:
                    board[i][j][k] = sums[k] - sums[j-1]
        else:
            max_value = -float('inf')
            for j2 in range(n):
                for k2 in range(n):
                    if k2 >= j-1:
                        continue
                    max_value = max(max_value, board[i-1][j2][k2])
            for k in range(j,n):
                if j == 0:
                    board[i][j][k] = max_value + sums[k]
                else:
                    board[i][j][k] = max_value + sums[k] - sums[j-1]


print(max([max(i) for i in board[-1]]))
