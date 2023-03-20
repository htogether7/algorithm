import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

cheese_count = sum([sum(board[i]) for i in range(n)])

def check_space(board):
    for r in range(n):
        for c in range(m):
            if board[r][c] != 0:
                continue
            outside_air = 3
            pos = set()
            
            queue = deque()
            queue.append((r,c))

            while queue:
                now_r,now_c = queue.popleft()
                for i in range(4):
                    next_r = now_r+dy[i]
                    next_c = now_c+dx[i]
                    if next_r < 0 or next_r >= n or next_c < 0 or next_c >= m:
                        outside_air = 2
                        continue
                    if (next_r, next_c) in pos:
                        continue
                    if board[next_r][next_c] == 1:
                        continue
                    queue.append((next_r,next_c))
                    pos.add((next_r,next_c))
            for y,x in pos:
                board[y][x] = outside_air

def delete_cheese(board):
    global cheese_count
    for r in range(1,n-1):
        for c in range(1,m-1):
            if board[r][c] != 1:
                continue
            count = 0
            for i in range(4):
                next_r = r+dy[i]
                next_c = c+dx[i]
                if board[next_r][next_c] == 2:
                    count+=1
            if count >= 2:
                board[r][c] = 0
                cheese_count -= 1

def initialize(board):
    for r in range(n):
        for c in range(m):
            if board[r][c] != 1:
                board[r][c] = 0

time = 0
while True:
    check_space(board)
    delete_cheese(board)
    if cheese_count == 0:
        print(time+1)
        break
    initialize(board)
    time += 1