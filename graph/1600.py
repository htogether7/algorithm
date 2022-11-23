import sys
from collections import deque
input = sys.stdin.readline

k = int(input())
w,h = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(h)]
check = [[0] * w for _ in range(h)]
q = deque([[0,0,k,0]])
check[0][0] = 1
dy = [1,-1,0,0]
dx = [0,0,1,-1]

dy_horse = [2,2,1,1,-1,-1,-2,-2]
dx_horse = [1,-1,2,-2,2,-2,1,-1]

count = 0
possible = False
while q:
    r,c,k_count,count = q.popleft()
    if r == h-1 and c == w-1:
        possible = True
        print(count)
        break

    for index in range(4):
        nr = r + dy[index]
        nc = c + dx[index]
        if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0:
            if (dy[index] < 0 or dx[index] < 0) and check[nr][nc] == 1:
                continue
            else:
                q.append([nr,nc,k_count,count+1])
                check[nr][nc] = 1

    if k_count > 0:
        for index in range(8):
            nr = r + dy_horse[index]
            nc = c + dx_horse[index]
            if 0 <= nr < h and 0 <= nc < w and board[nr][nc] == 0:
                if (dy_horse[index] < 0 or dx_horse[index] < 0) and check[nr][nc] == 1:
                    continue
                else:
                    q.append([nr,nc,k_count-1,count+1])
                    check[nr][nc] = 1
    # count += 1
    # if count == 2:
        # break

if not possible:
    print(-1)
# print(q)
# print(board)
# print(check)
    