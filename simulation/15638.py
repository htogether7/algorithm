import sys
n,m = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)]

cctvs = []
for row in range(n):
    for col in range(m):
        if board[row][col] != 0 and board[row][col] != 6:
            cctvs.append((board[row][col], (row,col)))

path = []

direction_count = {
    1 : 4,
    2 : 2,
    3:  4,
    4: 4,
    5: 1
}

def paint(board, direction, pos):
    ds = [(1,0), (-1,0), (0,1), (0,-1)]
    pos = [pos[0], pos[1]]
    while True:
        pos[0] += ds[direction][0]
        pos[1] += ds[direction][1]
        if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= m:
            return
        if board[pos[0]][pos[1]] == 6:
            return
        
        if board[pos[0]][pos[1]] == "#" or 1 <= board[pos[0]][pos[1]] <= 5:
            continue

        board[pos[0]][pos[1]] = "#"

        

    # if direction == 0:
        # while 

def count_area(path):
    # print(path)
    copy_board = [board[i][::] for i in range(n)]
    for direction, (kind, pos) in path:
        if kind == 1:
            paint(copy_board, direction, pos)
    
        elif kind == 2:
            if direction == 0:
                paint(copy_board, 0, pos)
                paint(copy_board, 1, pos)
            elif direction == 1:
                paint(copy_board, 2, pos)
                paint(copy_board, 3, pos)
        elif kind == 3:
            if direction == 0:
                paint(copy_board, 0, pos)
                paint(copy_board, 2, pos)
            elif direction == 1:
                paint(copy_board, 0, pos)
                paint(copy_board, 3, pos)
            elif direction == 2:
                paint(copy_board, 1, pos)
                paint(copy_board, 2, pos)
            elif direction == 3:
                paint(copy_board, 1, pos)
                paint(copy_board, 3, pos)
        elif kind == 4:
            for i in range(4):
                if i != direction:
                    paint(copy_board,i,pos)
        else:
            for i in range(4):
                paint(copy_board,i,pos)
        # print(direction, kind, pos)
    # print(copy_board)
    tmp_result = 0
    for row in range(n):
        for col in range(m):
            if copy_board[row][col] == 0:
                tmp_result += 1
    return tmp_result

answer = float('infinity')
def dfs(l):
    global path
    global answer
    if l == len(cctvs):
        # print(path)
        answer = min(answer,count_area(path))
        return
    
    for i in range(direction_count[cctvs[l][0]]):
        path.append((i, cctvs[l]))
        dfs(l+1)
        path.pop()
dfs(0)
print(answer)
# print(cctvs)
# print(board)