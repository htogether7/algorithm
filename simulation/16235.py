import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int, input().split())

plus = [list(map(int,input().split())) for _ in range(n)]

board = [[[5,[],0] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y,z = map(int,input().split())
    board[x-1][y-1][1].append(z)

for i in range(n):
    for j in range(n):
        board[i][j][1].sort()
        board[i][j][1] = deque(board[i][j][1])


def spring():
    for i in range(n):
        for j in range(n):
            if not board[i][j][1]:
                continue
            grown = deque()
            while board[i][j][1]:
                t = board[i][j][1].popleft()
                if t <= board[i][j][0]:
                    board[i][j][0] -= t
                    grown.append(t+1)
                else:
                    board[i][j][2] += (t // 2)
                    break
            for k in board[i][j][1]:
                board[i][j][2] += (k // 2)

            board[i][j][1] = grown


def summer():
    for i in range(n):
        for j in range(n):
            board[i][j][0] += board[i][j][2]
            board[i][j][2] = 0

def fall():
    dy = [-1,-1,-1,0,1,1,1,0]
    dx = [-1,0,1,1,1,0,-1,-1]
    for i in range(n):
        for j in range(n):
            for age in (board[i][j][1]):
                if age % 5 == 0:
                    for d in range(8):
                        next_y = i+dy[d]
                        next_x = j+dx[d]
                        if next_y < 0 or next_y >= n or next_x < 0 or next_x >=n:
                            continue
                        board[next_y][next_x][2] += 1

    for i in range(n):
        for j in range(n):
            for k in range(board[i][j][2]):
                board[i][j][1].appendleft(1)
            board[i][j][2] = 0


def winter():
    for i in range(n):
        for j in range(n):
            board[i][j][0] += plus[i][j]

for _ in range(k):
    spring()
    summer()
    fall()
    winter()

answer = 0
for i in range(n):
    for j in range(n):
        answer += len(board[i][j][1])
print(answer)