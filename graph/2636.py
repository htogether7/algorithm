import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(map(int,input().rstrip().split())) for _ in range(r)]
for i in range(r):
    board[i][0] = -1
    board[i][-1] = -1

for i in range(c):
    board[0][i] = -1
    board[-1][i] = -1

check = [[0] * c for _ in range(r)]
holes = [[0] * c for _ in range(r)]
# print(check)


def find_hole():
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    for row in range(1, r):
        for col in range(1, c):
            if check[row][col] == 0 and (board[row][col] == 0):
                paths = [(row,col)]
                isHole = True
                q = deque([(row,col)])
                check[row][col] = 1
                while q:
                    next_row, next_col = q.popleft()
                    paths.append((next_row,next_col))
                    for i in range(4):
                        if next_row+dy[i] == 0 or next_row+dy[i] == r or next_col+dx[i] == 0 or next_col+dx[i] == c:
                            isHole = False
                            continue
                        if board[next_row+dy[i]][next_col+dx[i]] == 1:
                            continue
                        if check[next_row+dy[i]][next_col+dx[i]] != 0:
                            continue
                        q.append((next_row+dy[i], next_col+dx[i]))
                        check[next_row+dy[i]][next_col+dx[i]] = 1
                if isHole:
                    for r1,c1 in paths:
                        holes[r1][c1] = 1

def check_sum():
    tmp_answer = 0
    for row in range(r):
        for col in range(c):
            if board[row][col] == 1:
                tmp_answer += 1
    return tmp_answer

def check_around(row,col):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    for i in range(4):
        if row+dy[i] == 0 or row+dy[i] == r-1 or col+dx[i] == 0 or col+dx[i] == c-1:
            return True
        
        if board[row+dy[i]][col+dx[i]] == 0 and holes[row+dy[i]][col+dx[i]] == 0:
            return True
    return False


def find_melting():
    for row in range(1,r):
        for col in range(1,c):
            if board[row][col] == 1:
                if check_around(row,col):
                    board[row][col] = 2

def melt():
    for row in range(1,r):
        for col in range(1,c):
            if board[row][col] == 2:
                board[row][col] = 0

prev_check_sum = check_sum()
time = 0
while True:
    check = [[0] * c for _ in range(r)]
    holes = [[0] * c for _ in range(r)]
    # if prev_check_sum == 0:
        # break
    # print(prev_check_sum)
    find_hole()
    find_melting()
    # print(board)
    melt()
    now_check_sum = check_sum()
    time += 1

    if now_check_sum == 0:
        print(time, prev_check_sum)
        break
    prev_check_sum = now_check_sum
    # print(board)
    # break

    
# find_hole()
# 
# print(check_sum())
# print(board)