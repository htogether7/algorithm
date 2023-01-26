import sys
from collections import deque, defaultdict

input = sys.stdin.readline

n, k = map(int, input().split())

board = [list(map(int,input().split())) for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]
global count_dict
count_dict = {}

def melt():
    global count_dict
    count_dict = {}
    for r in range(n):
        for c in range(k):
            if board[r][c] == 0:
                continue
            for i in range(4):
                next_r = r + dy[i]
                next_c = c + dx[i]
                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= k:
                    continue
                if board[next_r][next_c] != 0:
                    continue
                
                if (r,c) not in count_dict:
                    count_dict[(r,c)] = 1
                else:
                    count_dict[(r,c)] += 1

    # print(board,count_dict)
    for key in list(count_dict.keys()):
        r,c = key
        if count_dict[key] >= board[r][c]:
            board[r][c] = 0
            # del count_dict[(r,c)]
        else:
            board[r][c] -= count_dict[key]

def land_count():
    global count_dict
    count = 0
    count_set = set()
    # print(count_dict)
    for key in count_dict.keys():
        if count_dict[key] == 0:
            continue
        r,c = key
        if key in count_set:
            continue
        q = deque()
        q.append((r,c))
        count_set.add((r,c))
        while q:
            q_r,q_c = q.popleft()
            for i in range(4):
                next_r, next_c = q_r + dy[i], q_c + dx[i]
                if next_r < 0 or next_r >= n or next_c < 0 or next_c >= k:
                    continue
                if board[next_r][next_c] == 0:
                    # print(next_r,next_c)
                    continue
                if (next_r,next_c) in count_set:
                    continue
                q.append((next_r,next_c))
                count_set.add((next_r,next_c))
                
            if len(q) == 0:
                count += 1
            # print(count, q_r,q_c)
            # print(q, count_set, count_dict)
        if count >= 2:
            break
        # print(board)
    if count >= 2:
        return True
    else:
        return False


year_count = 0
while True:
    melt()
    # print(board)
    # print(count_dict)
    # if len(count_dict.keys()) <= 1:
    # print(count_dict)
   
    year_count += 1
    if land_count():
        print(year_count)
        break
    
    for key in count_dict:
        if count_dict[key] == 0:
            del count_dict[key]

    if not count_dict:
        print(0)
        # print(year_count)
        break