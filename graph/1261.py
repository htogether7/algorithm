import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
board = [list(map(int,input().rstrip())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

check[0][0] = 1

dy = [1,-1,0,0]
dx = [0,0,1,-1]

answer = float('inf')

def dfs(y,x,count):
    global answer
    # print(check)
    if y == n-1 and x == m-1:
        # print(count)
        print(check)
        answer = min(answer, count)
        return
    
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if next_y < 0 or next_y >= n or next_x < 0 or next_x >=m:
            continue
        if check[next_y][next_x] == 1:
            # continue
            continue

        if board[next_y][next_x] == 1:
            check[next_y][next_x] = 1
            dfs(next_y,next_x,count+1)
            check[next_y][next_x] = 0
        else:
            check[next_y][next_x] = 1
            dfs(next_y, next_x, count)
            check[next_y][next_x] = 0
        # dfs()
dfs(0,0,0)
print(answer)