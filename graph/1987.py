import sys
from collections import defaultdict
input = sys.stdin.readline
r,c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]

dy = [1,-1,0,0]
dx = [0,0,1,-1]

# dict = defaultdict(int)
check = [[0] * c for _ in range(r)]
check[0][0] = 1
arr = [0] * 26
arr[ord(board[0][0])-65] = 1
# dict[board[0][0]] += 1

answer = 0

def dfs(l, pos):
    global answer
    check_possible = False
    for i in range(4):
        next_y = pos[0] + dy[i]
        next_x = pos[1] + dx[i]
        if 0 <= next_y < r and 0 <= next_x < c and arr[ord(board[next_y][next_x])-65] == 0:
            check_possible = True
            arr[ord(board[next_y][next_x])-65] = 1
            # check[next_y][next_x] = 1
            dfs(l+1, [next_y,next_x])
            # print(next_y, next_x, l+2, dict, check)
            # answer = max(answer, l+2)
            # if l+2 > answer:
                # answer = l+2
            arr[ord(board[next_y][next_x])-65] = 0
            # check[next_y][next_x] = 0
    if not check_possible:
        answer = max(answer, l+1)
        # print(l+1, pos)
dfs(0,[0,0])
print(answer)
# print(board)


                
from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

Board = [list(map(str, input().strip())) for _ in range(N)]

def to_num(x, y):
    return ord(Board[x][y]) - ord('A')	


visited = [0] * 26
visited[to_num(0,0)] = 1
answer = 1


def DFS(currX, currY, depth):
	global answer
	
	dx, dy = [1,-1,0,0], [0,0,1,-1]
	
	for i in range(4):
		xx, yy = currX + dx[i], currY + dy[i]
		
		if xx >=N or yy >= M or xx < 0 or yy < 0:
			continue
			
		if visited[to_num(xx,yy)] != 1:
			visited[to_num(xx,yy)] = 1
			DFS(xx, yy, depth+1)
			visited[to_num(xx,yy)] = 0
		
	answer = max(answer, depth)
	
DFS(0,0,1)
print(answer)