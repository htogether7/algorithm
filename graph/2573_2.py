import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(n)]

melt_check_dict = {}

dy = [1,-1,0,0]
dx = [0,0,1,-1]

def ice_check():
    global melt_check_dict
    melt_check_dict = {}
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                count = 0
                for ind in range(4):
                    next_y = i + dy[ind]
                    next_x = j + dx[ind]
                    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                        continue

                    if board[next_y][next_x] == 0:
                        count+=1
                # if count == 0:
                    # continue
                melt_check_dict[(i,j)] = count


def melt():      
    key_list = list(melt_check_dict.keys())  
    for key in key_list:
        r,c = key
        if melt_check_dict[key] >= board[r][c]:
            board[r][c] = 0
            del melt_check_dict[key]
        else:
            board[r][c] -= melt_check_dict[key]
        # 
        # pass
def check_seperate():
    check_pos = set()
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                continue
            q = deque()
            q.append((i,j))
            check_pos.add((i,j))
            while q:
                r,c = q.popleft()
                for ind in range(4):
                    next_y = r + dy[ind]
                    next_x = c + dx[ind]

                    if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                        continue

                    if board[next_y][next_x] == 0:
                        continue

                    if (next_y,next_x) in check_pos:
                        continue

                    check_pos.add((next_y,next_x))
                    q.append((next_y,next_x))
            # print(check_pos)
            if len(check_pos) != len(melt_check_dict):
                return True
            else:
                return False

                



# print(board)
# ice_check()
# print(melt_check_dict)
# melt()
# ice_check()
# print(melt_check_dict)
# print(board)
# print(melt_check_dict)
def check_melt_possible():
    for key in melt_check_dict:
        if melt_check_dict[key] > 0:
            return True
    return False

ice_check()
year_count = 0
# print(melt_check_dict)
while True:
    # print("hi")
    if check_seperate():
        print(year_count)
        break
    melt()
    year_count += 1
    ice_check()

    if not melt_check_dict:
        print(0)
        break
    # print(board)
    # print(melt_check_dict)
    # roof_count += 1
    # if roof_count == 2:
    #     break