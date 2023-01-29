import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

key_set = set()
door_set = set()

cannot_set = set()
cannot_set.add("#")

start = (-1,-1)

for i in range(n):
    for j in range(m):
        # if board[i][j] == 
        # pass
        if 65 <= ord(board[i][j]) <= 70:
            door_set.add(board[i][j])
        
        if 97 <= ord(board[i][j]) <= 102:
            key_set.add(board[i][j])
        
        if board[i][j] == "0":
            start = (i,j)


for door in door_set:
    if chr(ord(door)+32) not in key_set:
        cannot_set.add(door)



def bfs():
    # count = 0
    check = [[0] * m for _ in range(n)]
    q = deque()
    q.append((start, 0, [0,0,0,0,0,0]))
    check[start[0]][start[1]] = (0,[0,0,0,0,0,0])

    while q:
        now_pos, now_count, now_key = q.popleft()
        for i in range(4):
            next_y = now_pos[0] + dy[i]
            next_x = now_pos[1] + dx[i]
            if next_y < 0 or next_y >= n or next_x < 0 or next_x >= m:
                continue

            if board[next_y][next_x] in cannot_set:
                continue

            if board[next_y][next_x] == '1':
                return now_count+1

            if board[next_y][next_x] in door_set:
                if now_key[ord(board[next_y][next_x]) - 65] == 0:
                    continue

            if check[next_y][next_x] != 0:
                check_revisit = True
                for i in range(len(now_key)):
                    if now_key[i] == 0 :
                        continue
                    if check[next_y][next_x][1][i] == 0:
                        check_revisit = False
                if check_revisit:
                    continue
                # if now_count + 1 >= check[next_y][next_x][0]:
                    # continue

            if board[next_y][next_x] in key_set:
                # now_key.add(board[next_y][next_x])
                copy_key = now_key[::]
                copy_key[ord(board[next_y][next_x])-97] = 1
                
                check[next_y][next_x] = (now_count+1, copy_key)
                q.append(((next_y,next_x), now_count+1, copy_key))
            else:
                check[next_y][next_x] = (now_count+1, now_key)
                q.append(((next_y,next_x), now_count+1, now_key))


                    # check[next_y][next_x] = ()
        # print(check)
        # count += 1
        # if count == 30:
            # break
    return -1

print(bfs())

# print(check)
# print(set('a') == set('a'))

# print(cannot_set)
# print(key_set)
# print(door_set)

# print(ord('F'))
# print(board)