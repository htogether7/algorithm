import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int, input().split())

check = [[[-1] * 4 for _ in range(c)] for _ in range(r)]

board = [list(map(int, input().split())) for _ in range(r)]

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

s_r, s_c, s_d = map(int,input().split())
e_r, e_c, e_d = map(int,input().split())

q = deque()
check[s_r-1][s_c-1][s_d-1] = 0
q.append((s_r-1, s_c-1, s_d-1,0))

def turn_left(dir):
    if dir == 0:
        return 3
    elif dir == 3:
        return 1
    elif dir == 1:
        return 2
    elif dir == 2:
        return 0
    
def turn_right(dir):
    if dir == 0:
        return 2
    elif dir == 2:
        return 1
    elif dir == 1:
        return 3
    elif dir == 3:
        return 0


while q:
    # print(q)
    now_r,now_c,now_d,count = q.popleft()
    if now_r == e_r-1 and now_c == e_c-1 and now_d == e_d-1:
        print(count)
        break

    # Go k
    for k in range(1,4):
        dr, dc = dirs[now_d]
        next_r = now_r + dr * k
        next_c = now_c + dc * k
        if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
            continue

        if board[next_r][next_c] == 1:
            break

        if 0 <= check[next_r][next_c][now_d] <= count+1:
            continue

        check[next_r][next_c][now_d] = count+1
        q.append((next_r, next_c, now_d, count+1))

    # Turn Dir
    for i, d in enumerate([turn_left(now_d), turn_left(turn_left(now_d)), turn_right(now_d)]):
        if 0 <= check[now_r][now_c][d] <= count+1:
            continue
        p = 1
        if i == 1:
            p = 2
        check[now_r][now_c][d] = count+p
        q.append((now_r, now_c, d, count+p))
