import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip())for _ in range(n)]

path = []
start_blue_pos = []
start_red_pos = []

for r in range(n):
    for c in range(m):
        if board[r][c] == "B":
            start_blue_pos = [r,c]
        if board[r][c] == "R":
            start_red_pos = [r,c]

def move_y(dy, pos):
    global board
    start_y, start_x = pos[0]
    now_y, now_x = pos[0]
    board[start_y][start_x] = "."
    while True:
        if board[now_y+dy][start_x] == "O":
            board[start_y][start_x] == "."
            return -1
        
        if board[now_y+dy][start_x] != ".":
            break
        now_y += dy
    board[now_y][start_x] = pos[1]
    return [now_y, start_x]

    
def move_x(dx, pos):
    global board
    start_y, start_x = pos[0]
    now_y, now_x = pos[0]
    board[start_y][start_x] = "."
    while True:

        if board[start_y][now_x+dx] == "O":
            board[start_y][start_x] = "."
            return -1
        if board[start_y][now_x+dx] != ".":
            break
        now_x +=dx
    board[start_y][now_x] = pos[1]
    return [start_y,now_x]


def check_possible(direction, red_pos, blue_pos):
    dys = [1,-1,0,0]
    dxs = [0,0,1,-1]
    dy = dys[direction]
    dx = dxs[direction]
    positions = [(red_pos,"R"), (blue_pos,"B")]
    next_red_pos = []
    next_blue_pos = []

    if dx == 0:
        if red_pos[1] == blue_pos[1]:
            if dy == -1:
                positions.sort(key = lambda x : x[0][0])
            else:
                positions.sort(key = lambda x : -x[0][0])

        for pos in positions:
            tmp_pos = move_y(dy, pos)
            if pos[1] == "B":
                next_blue_pos = tmp_pos
            else:
                next_red_pos = tmp_pos

    else:
        if red_pos[0] == blue_pos[0]:
            if dx == -1:
                positions.sort(key = lambda x : x[0][1])
            else:
                positions.sort(key = lambda x : -x[0][1])

        for pos in positions:
            tmp_pos = move_x(dx, pos)
            if pos[1] == "B":
                next_blue_pos = tmp_pos
            else:
                next_red_pos = tmp_pos

    return [next_red_pos, next_blue_pos]
        

answer = 11

def erase(board, positions):
    for pos in positions:
        if pos == -1:
            continue
        y,x = pos
        board[y][x] = "."

real_path = []
def backtracking(l, red_pos, blue_pos):
    global board
    global path
    global answer
    if l == 10:
        return
    
    for i in range(4):
        if len(path) > 0 and path[-1][0]//2 == i//2:
            continue
        prev_red_pos, prev_blue_pos = red_pos, blue_pos
        next_red_pos, next_blue_pos = check_possible(i, red_pos, blue_pos)
        if prev_blue_pos == next_blue_pos and prev_red_pos == next_red_pos:
            continue

        path.append([i, next_red_pos, next_blue_pos])
        real_path.append(i)
        if next_red_pos == -1 and next_blue_pos != -1:
            # 성공으로 끝남
            answer = min(answer, len(path))
            _, next_red_pos, next_blue_pos = path.pop()
            real_path.pop()
            erase(board, [next_red_pos, next_blue_pos])
            return
        elif next_blue_pos == -1:
            # 실패로 끝남
            _, next_red_pos, next_blue_pos = path.pop()
            real_path.pop()
            erase(board, [next_red_pos, next_blue_pos])
            continue
        else:
            # 안 끝남
            backtracking(l+1, next_red_pos, next_blue_pos)
            _, next_red_pos, next_blue_pos = path.pop()
            real_path.pop()
            erase(board, [next_red_pos, next_blue_pos])

backtracking(0, start_red_pos, start_blue_pos)
if answer == 11:
    print(-1)
else:
    print(answer)