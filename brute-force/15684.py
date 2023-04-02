import sys
n,m,h = map(int, input().split())
path = [list(map(int,input().split())) for _ in range(m)]
board = [[0] * (n-1) for _ in range(h)]

for a,b in path:
    board[a-1][b-1] = 1

answer = -1

def find_possible():
    possible_path = []
    for i in range(h):
        for j in range(n-1):
            if board[i][j] == 1:
                continue
            check_possible = True
            if j-1 >= 0:
                if board[i][j-1] != 0:
                    check_possible = False
            
            if j+1 < n-1:
                if board[i][j+1] != 0:
                    check_possible = False

            if check_possible:
                possible_path.append((i,j))
    return possible_path
    
possible_path = find_possible()

def go_down(board):
    order = [i for i in range(n)]

    for i in range(h):
        for j in range(n-1):
            if board[i][j] == 1:
                order[j], order[j+1] = order[j+1], order[j]
    # print(order)
    for i, num in enumerate(order):
        if i != num:
            return False
    return True

def check_possible(path_arr):
    copy_board = [board[i][::] for i in range(h)]
    for path in path_arr:
        i,j = path
        copy_board[i][j] = 1
    return go_down(copy_board)

def choose_path(n):
    chosen_path = []
    global answer

    def dfs(s,l):
        global answer
        if l == n:
            if check_possible(chosen_path):
                answer = n
            return 
        
        if s >= len(possible_path):
            return
        for i in range(s,len(possible_path) - n + l+1):
            check_pass = False
            for path in chosen_path:
                if possible_path[i][0] == path[0] and abs(possible_path[i][1] - path[1]) == 1:
                    check_pass = True
            if check_pass:
                continue
            chosen_path.append(possible_path[i])

            dfs(i+1, l+1)
            chosen_path.pop()
    dfs(0,0)

for i in range(4):
    # print(i)
    choose_path(i)
    if answer != -1:
        print(i)
        break

if answer == -1:
    print(-1)