import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

end = []
start = []
waters = []

for row in range(r):
    for col in range(c):
        if board[row][col] == "D":
            end = [row,col]
        elif board[row][col] == "S":
            start = [row,col]
        elif board[row][col] == "*":
            waters.append([row,col])

queue = deque([(start, 0)])


dy = [1,-1,0,0]
dx = [0,0,1,-1]
answer = 2500

def water_spread(board,waters):
    next_water = []
    for (y,x) in waters:
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                continue
            if board[next_y][next_x] == "D" or board[next_y][next_x] == "X" or board[next_y][next_x] == "*":
                continue 
            board[next_y][next_x] = "*"
            next_water.append([next_y,next_x])
    waters.extend(next_water)

    return waters



def move(board,queue):
    global answer
    next_queue = deque()
    # print(board)
    while queue:
        [now_y, now_x], time = queue.popleft()
        # print(now_y,now_x)
        for i in range(4):
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if next_y < 0 or next_y >= r or next_x < 0 or next_x >= c:
                continue
            if board[next_y][next_x] == "S" or board[next_y][next_x] == "*":
                continue
            if board[next_y][next_x] == "D":
                answer = min(answer, time+1)
            if board[next_y][next_x] == ".":
                next_queue.append([[next_y,next_x], time+1])
                board[next_y][next_x] = "S"
        # print(next_queue)
    return next_queue
            


while True:
    # print(board)
    waters = water_spread(board, waters)
    queue = move(board,queue)

    if answer != 2500:
        print(answer)
        break
    
    if not queue:
        print("KAKTUS")
        break
    
    

        # for i in range(4)

# print(board)