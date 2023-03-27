import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int , input().split())

board = [list(input().rstrip()) for _ in range(r)]

answer = 0
dy = [1,-1,0,0]
dx = [0,0,1,-1]

for row in range(r):
    for col in range(c):
        if board[row][col] == "W":
            continue
        q = deque()
        check  = [[0] * c for _ in range(r)]
        check[row][col] = 1
        q.append((row,col,0))
        while q:
            y,x,time = q.popleft()
            answer = max(answer, time)
            for i in range(4):
                next_y, next_x = y+dy[i], x+dx[i]
                if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                    continue
                if board[next_y][next_x] == "W":
                    continue
                if check[next_y][next_x] == 1:
                    continue
                
                q.append((next_y,next_x,time+1))
                check[next_y][next_x] = 1

print(answer)