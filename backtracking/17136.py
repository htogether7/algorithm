import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(10)]

papers = [-1,5,5,5,5,5]

def check_max_size(r,c):
    for i in range(1,5):
        if r+i >= 10 or c+i >= 10:
            return i
        
        check_possible = True
        for y in range(r, r+i):
            if board[y][c+i] == 0:
                check_possible = False
        
        for x in range(c, c+i):
            if board[r+i][x] == 0:
                check_possible = False
        
        if board[r+i][c+i] == 0:
            check_possible = False

        if not check_possible:
            return i
    return 5


answer = 25

pos = []

def dfs():


    pos.append(())
    dfs()
    pos.pop()

def fill(i,j,l):
    global pos
    tmp_set = {}
    for r in range(i, i+l):
        for c in range(j, j+l):
            tmp_set.add((r,c))
    
    pos.append(tmp_set)

for i in range(10):
    for j in range(10):
        if board[i][j] == 0:
            continue
        limit = check_max_size(i,j)
        for l in range(1,limit+1):
            fill(i,j,l)




# print(board)