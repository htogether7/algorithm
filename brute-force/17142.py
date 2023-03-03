import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

viruses = []

for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            viruses.append((r,c))


selected_virus = []

def move_virus(board, selected_virus):
    copy_board = [[0] * n for _ in range(n)]
    live_virus_set = set()
    for index in selected_virus:
        live_virus_set.add(viruses[index])
    
    q = deque([])
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]
    count = 0

    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                copy_board[r][c] = '-'
            elif board[r][c] == 2:
                if (r,c) in live_virus_set:
                    copy_board[r][c] = "l"
                    q.append((r,c,0))
                else:
                    copy_board[r][c] = "d"
            else:
                count += 1

    time = -1
    while q:
        if time != q[0][2]:
            if count == 0:
                return time+1
            else:
                time += 1 
        now_y, now_x, now_time = q.popleft()
        for i in range(4):
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= n:
                continue
            if copy_board[next_y][next_x] in ["-", "l"]:
                continue
            if copy_board[next_y][next_x] != "d":
                count -= 1
            copy_board[next_y][next_x] = "l"
            q.append((next_y,next_x,now_time+1))
    return float('infinity')


answer = float('inf')

def dfs(l,s):
    global answer
    if l == m:
        answer = min(answer, move_virus(board, selected_virus))
        return
    for i in range(s, len(viruses)-(m-l)+1):
        selected_virus.append(i)
        dfs(l+1,i+1)
        selected_virus.pop()

dfs(0,0)
if answer == float('inf'):
    print(-1)
else:
    print(answer)