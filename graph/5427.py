import sys
input = sys.stdin.readline

result = []
t = int(input())

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def move_fire(board, fire_pos_set):
    next_set = set()
    for y,x in fire_pos_set:
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
                continue
            if board[next_y][next_x] == "#" or board[next_y][next_x] == "*":
                continue
            next_set.add((next_y,next_x))
            board[next_y][next_x] = "*"
    return next_set


def move(board, sk_pos_set):
    next_set = set()
    for y,x in sk_pos_set:
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if board[next_y][next_x] == ".":
                board[next_y][next_x] = "@"
                next_set.add((next_y,next_x))

    return next_set


def check_move_out(board, sk_pos_set):
    for y,x in sk_pos_set:
        for i in range(4):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y < 0 or next_y >= h or next_x < 0 or next_x >= w:
                return True
    return False


def make_pos_set(board, sym):
    tmp_set = set()
    for r in range(h):
        for c in range(w):
            if board[r][c] == sym:
                tmp_set.add((r,c))
    return tmp_set


for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(h)]
    fire_pos_set = make_pos_set(board, "*")
    sk_pos_set = make_pos_set(board, "@")

    time = 0
    while True:
        if check_move_out(board, sk_pos_set):
            result.append(time+1)
            break
        fire_pos_set = move_fire(board, fire_pos_set)
        sk_pos_set = move(board, sk_pos_set)
        if not sk_pos_set:
            result.append("IMPOSSIBLE")
            break
        time += 1

for r in result:
    print(r)

