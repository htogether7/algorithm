import sys
from collections import deque
input = sys.stdin.readline

board = []
for _ in range(4):
    tmp = []
    a1,b1, a2,b2, a3,b3, a4,b4 = map(int, input().split())
    tmp.append((a1,b1))
    tmp.append((a2,b2))
    tmp.append((a3,b3))
    tmp.append((a4,b4))
    board.append(tmp)

dict = {}

for r in range(4):
    for c in range(4):
        dict[board[r][c][0]] = (r,c)

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,-1,-1,-1,0,1,1,1]

shark_pos = (0,0,board[0][0][1])
answer = board[0][0][0]
del dict[board[0][0][0]]
board[0][0] = ("s",shark_pos[2])

def move_fish(board, dict):
    keys = list(dict.keys())
    keys.sort()
    for num in keys:
        y,x = dict[num]
        _, dir = board[y][x]
        count = 0
        while True:
            next_y = y + dy[dir-1]
            next_x = x + dx[dir-1]
            if 0 <= next_y < 4 and 0 <= next_x < 4 and board[next_y][next_x][0] not in ["s"] :
                # switch
                if board[next_y][next_x][0] == "":
                    dict[num] = (next_y,next_x)
                else:
                    dict[num], dict[board[next_y][next_x][0]] = dict[board[next_y][next_x][0]], dict[num]
                board[y][x], board[next_y][next_x] = board[next_y][next_x], board[y][x]
                break
            else:
                count += 1
                dir = (dir % 8) + 1
                board[y][x] = (board[y][x][0], dir)
                if count == 8:
                    break


move_fish(board, dict)        

q = deque()
q.append((board, dict, answer, shark_pos))

while q:
    now_board, now_dict, count, pos = q.popleft()
    answer = max(answer, count)
    next_nodes = []
    y,x,d = pos
    init_y = y
    init_x = x
    while True:
        y += dy[d-1]
        x += dx[d-1]
        if y < 0 or y >= 4 or x < 0 or x >= 4:
            break
        if now_board[y][x][0] not in ["s", ""]:
            next_nodes.append((y,x))
    
    for (next_y,next_x) in next_nodes:
        next_num = now_board[next_y][next_x][0]
        next_pos = (next_y,next_x,now_board[next_y][next_x][1])
        next_count = count + next_num
        next_board = [now_board[i][::] for i in range(4)]
        next_dict = {}
        for key in now_dict:
            next_dict[key] = now_dict[key]
        
        del next_dict[next_num]
        next_board[init_y][init_x] = ("","")
        next_board[next_y][next_x] = ("s", next_board[next_y][next_x][1])
        move_fish(next_board, next_dict)
        q.append((next_board, next_dict, next_count, next_pos))
print(answer)