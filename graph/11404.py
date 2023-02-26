import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

board = [[float('infinity')] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    # print(board[a][b])
    board[a][b] = min(board[a][b], c)

for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            board[a][b] = min(board[a][b], board[a][k]+ board[k][b])
            if a== b:
                board[a][b] = 0
for a in range(n+1):
    for b in range(n+1):
        if board[a][b] == float('infinity'):
            board[a][b] = 0
# print(board)
for r in range(1, n+1):
    print(*map(str,board[r][1:]))
    # print(board[r][1:].join(" "))
    # print(" ".join(board[r]))
# print(board)