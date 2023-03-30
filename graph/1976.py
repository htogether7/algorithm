import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

board = [list(map(int,input().split())) for _ in range(n)]

order = list(map(int,input().split()))

for k in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if board[a][k] == 1 and board[k][b] == 1:
                board[a][b] = 1
                
for i in range(len(order)-1):
    if order[i] == order[i+1]:
        continue
    if board[order[i]-1][order[i+1]-1] == 0:
        print("NO")
        exit(0)
print("YES")
