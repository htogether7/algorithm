import sys
from collections import deque
input = sys.stdin.readline

board = [list(input().rstrip()) for _ in range(12)]
dy = [1,-1,0,0]
dx = [0,0,1,-1]


def find_groups(board):
    pos = set()
    check = set()
    for r in range(12):
        for c in range(6):
            if board[r][c] == ".":
                continue
            if (r,c) in check:
                continue

            q = deque()
            color = board[r][c]
            tmp_pos = set()
            tmp_pos.add((r,c))
            q.append((r,c))
            check.add((r,c))
            while q:
                now_r,now_c = q.popleft()
                for i in range(4):
                    next_r = now_r + dy[i]
                    next_c = now_c + dx[i]
                    if next_r < 0 or next_r >= 12 or next_c < 0 or next_c >= 6:
                        continue
                    if board[next_r][next_c] != color:
                        continue
                    if (next_r,next_c) in check:
                        continue
                    if (next_r,next_c) in tmp_pos:
                        continue
                    q.append((next_r,next_c))
                    tmp_pos.add((next_r,next_c))
                    check.add((next_r,next_c))
            if len(tmp_pos) >= 4:
                pos = pos.union(tmp_pos)
    return pos


def boom(pos,board):
    for y,x in pos:
        board[y][x] = "."


def move_down(board):
    for r in range(11,-1,-1):
        for c in range(6):
            if board[r][c] == ".":
                continue
            after_move_r = r
            color = board[r][c]
            while True:
                if after_move_r == 11:
                    break
                
                if board[after_move_r+1][c] != ".":
                    break

                after_move_r += 1
            board[r][c] = "."
            board[after_move_r][c] = color


count = 0
while True:
    pos = find_groups(board)
    if not pos:
        break
    boom(pos,board)
    move_down(board)
    count +=1

print(count)

