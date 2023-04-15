import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())

board = [[0] * m for _ in range(n)]
count = 0

def rotate_sticker(sticker):
    w = len(sticker[0])
    h = len(sticker)

    rotated_sticker = [[0] * h for _ in range(w)]

    for r in range(h):
        for c in range(w):
            rotated_sticker[c][h-1-r] = sticker[r][c]
    return rotated_sticker

def paint_board(board,sticker,r,c):
    w = len(sticker[0])
    h = len(sticker)
    for row in range(h):
        for col in range(w):
            if sticker[row][col] == 0:
                continue
            board[row+r][col+c] = 1


def check_possible(board,sticker,r,c):
    w = len(sticker[0])
    h = len(sticker)
    for row in range(h):
        for col in range(w):
            if sticker[row][col] == 0:
                continue
            if board[row+r][col+c] == 1:
                return False
    return True

def find_space(board, sticker):
    for r in range(n-len(sticker)+1):
        for c in range(m-len(sticker[0])+1):
            if check_possible(board,sticker,r,c):
                paint_board(board,sticker,r,c)
                return True
    return False


for _ in range(k):
    r,c = map(int, input().split())
    sticker = [list(map(int,input().split())) for _ in range(r)]
    rotate_count = 0
    while rotate_count <= 3:
        if find_space(board,sticker):
            break
        else:
            sticker = rotate_sticker(sticker)
            rotate_count += 1

answer = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            answer += 1
print(answer)
