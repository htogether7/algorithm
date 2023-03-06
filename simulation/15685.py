import sys
input = sys.stdin.readline

n = int(input())
board = [[0] * 101 for _ in range(101)]
# print(board)
direction_dict = {
    0: (0,1),
    1: (-1,0),
    2: (0,-1),
    3: (1,0)
}


def move(board):
    x,y,d,g = map(int,input().split())
    board[y][x] = 1
    dy,dx = direction_dict[d]
    board[y+dy][x+dx] = 1
    end_point = (y+dy, x+dx)
    path = [d]
    generation = 0
    while generation < g:
        # 회전
        for index in range(len(path)-1, -1, -1):
            next_d = (path[index] + 1) % 4
            path.append(next_d)
            dy, dx = direction_dict[next_d]
            now_y, now_x = end_point
            next_y, next_x = now_y+dy, now_x+dx
            end_point = (next_y, next_x)
            board[next_y][next_x] = 1
        generation += 1


def check_points(board):
    answer = 0
    for r in range(100):
        for c in range(100):
            if board[r][c] == 1 and board[r+1][c] == 1 and board[r][c+1] == 1 and board[r+1][c+1] == 1:
                answer += 1
    return answer

for _ in range(n):
    move(board)

print(check_points(board))
# print(board)






