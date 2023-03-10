import sys
input = sys.stdin.readline

n,m = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

path = []
positions = []
for r in range(n):
    for c in range(m):
        if board[r][c] == "o":
            positions.append((r,c))

dys = [1,-1,0,0]
dxs = [0,0,1,-1]

answer = 11

def is_out(pos, direction):
    y,x = pos
    next_y = y + dys[direction]
    next_x = x + dxs[direction]
    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
        return True
    else:
        return False

def move(pos, direction):
    y,x = pos
    next_y = y + dys[direction]
    next_x = x + dxs[direction]
    if board[next_y][next_x] == "#":
        return pos
    else:
        return (next_y,next_x) 
    
def paint(positions, s):
    global board
    for pos in positions:
        y,x = pos
        board[y][x] = s


def backtracking(l, positions):
    global answer
    if l == 10:
        return
    for i in range(4):
        if len(path) > 0 and path[-1] == i:
            continue
        pos_1, pos_2 = positions
        is_out_1 = is_out(pos_1, i)
        is_out_2 = is_out(pos_2, i)
        if (is_out_1 and not is_out_2) or (is_out_2 and not is_out_1):
            answer = min(answer, l+1)
        elif is_out_1 and is_out_2:
            continue
        else:
            next_pos_1 = move(pos_1, i)
            next_pos_2 = move(pos_2, i)
            if next_pos_1 == next_pos_2:
                continue
            next_positions = [next_pos_1,next_pos_2]
            path.append((i, next_positions))
            paint(positions, ".")
            paint(next_positions, "o")
            
            backtracking(l+1, next_positions)
            _, next_positions = path.pop()
            paint(next_positions, ".")
            paint(positions, "o")

backtracking(0, positions)
if answer == 11:
    print(-1)
else:
    print(answer)
