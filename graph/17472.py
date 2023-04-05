import sys
from collections import deque, defaultdict
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]
number_of_island = 0

def paint(board,r,c, count):
    dy = [1,-1,0,0]
    dx = [0,0,1,-1]

    q = deque()
    q.append((r,c))
    board[r][c] = count
    while q:
        now_y,now_x = q.popleft()
        for i in range(4):
            next_y = now_y + dy[i]
            next_x = now_x + dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                continue
            if board[next_y][next_x] == 1:
                q.append((next_y,next_x))
                board[next_y][next_x] = count

def number_island(board):
    global number_of_island
    count = 2
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1:
                paint(board,r,c,count)
                count += 1
                number_of_island += 1


def find_path(board):
    path = defaultdict(int)

    # 가로선
    for r in range(n):
        start = -1
        count = 0
        for c in range(m):
            if board[r][c] == 0 and start == -1:
                start = c
                count = 1
            elif board[r][c] == 0:
                count += 1
            elif board[r][c] != 0:
                if start != 0 and count >= 2:
                    pos = (min(board[r][start-1], board[r][c])-1, max(board[r][start-1], board[r][c])-1)
                    if pos in path:
                        path[pos] = min(path[pos],count)
                    else:
                        path[pos] = count
                start = -1
                count = 0

    # 세로선
    for c in range(m):
        start = -1
        count = 0
        for r in range(n):
            if board[r][c] == 0 and start == -1:
                start = r
                count = 1
            elif board[r][c] == 0:
                count += 1
            elif board[r][c] != 0:
                if start != 0 and count >= 2:

                    pos = (min(board[start-1][c], board[r][c])-1, max(board[start-1][c], board[r][c])-1)
                    if pos in path:
                        path[pos] = min(path[pos],count)
                    else:
                        path[pos] = count
                start = -1
                count = 0
    return path

def check_zero(check):
    for i in range(1,len(check)):
        if check[i] == 0:
            return True
    return False

def find(x, check):
    if check[x] == x:
        return x
    check[x] = find(check[x],check)
    return check[x]

def union(x,y, check):
    X = find(x, check)
    Y = find(y, check)
    if X == Y:
        return
    else:
        if X < Y:
            check[Y] = X
        else:
            check[X] = Y

def is_union(x,y, check):
    if find(x,check) == find(y,check):
        return True
    else:
        return False


def cal_connect_min_value(board):
    answer = 0
    path = find_path(board)
    items = list(path.items())
    items.sort(key = lambda x : x[1])
    check = [i for i in range(number_of_island+1)]
    for pos, l in items:
        x,y = pos
        if is_union(x,y, check):
            continue
        union(x,y, check)
        answer += l
    for i in range(1, number_of_island+1):
        if find(i,check) != 1:
            return -1

    return answer

number_island(board)
print(cal_connect_min_value(board))