import sys
from collections import deque
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(3)]

dy = [-1,0,1,0]
dx = [0,1,0,-1]

def find_start(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i,j)
            
def check_finish(board):
    if board[0] == [1,2,3] and board[1] == [4,5,6] and board[2] == [7,8,0]:
        return True
    return False

def flat(board):
    arr = []
    arr += board[0]
    arr += board[1]
    arr += board[2]
    return arr


def bfs(board):
    if check_finish(board):
        return 0
    
    s = find_start(board)
    check = set()
    check.add("".join(map(str,flat(board))))

    q = deque()

    q.append((s,board,-1,0))
    count = 0

    while q:
        pos, b, d, c = q.popleft()
        y,x = pos

        for i in range(4):
            next_y = y + dy[i]
            next_x = x + dx[i]
            if next_y < 0 or next_y >= 3 or next_x < 0 or next_x >= 3:
                continue

            if d != -1 and abs(d-i) == 2:
                continue

            copy_board = [arr[::] for arr in b]
            copy_board[next_y][next_x], copy_board[y][x] = copy_board[y][x], copy_board[next_y][next_x]
            
            flat_copy_board = "".join(map(str,flat(copy_board)))
            if flat_copy_board in check:
                continue

            if check_finish(copy_board):
                return c+1

            q.append(((next_y,next_x), copy_board, i, c+1))
            check.add(flat_copy_board)

    return -1

print(bfs(board))