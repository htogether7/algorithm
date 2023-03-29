import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

def make_board(s):
    return [[s] * 3 for _ in range(3)]

def rotate(boards, direction):
    rotate_board ,rotate_direction = list(direction)
    if rotate_board == "L":
        board_sum_arr = deque()
        for i,board in enumerate(boards):
            tmp_arr = []
            if i == 3:
                for r in range(2,-1,-1):
                    tmp_arr.append((board[r][2]))
            else:
                for r in range(3):
                    tmp_arr.append(board[r][0])
            board_sum_arr.append(tmp_arr)
        if rotate_direction == "+":
            board_sum_arr.rotate(1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(-1)

        for i in range(4):
            if i != 3:
                for j in range(3):
                    boards[i][j][0] = board_sum_arr[i][j]
            else:
                for j in range(3):
                    boards[i][2-j][2] = board_sum_arr[i][j]

    elif rotate_board == "R":
        board_sum_arr = deque()
        for i,board in enumerate(boards):
            tmp_arr = []
            if i == 3:
                for r in range(2,-1,-1):
                    tmp_arr.append((board[r][0]))
            else:
                for r in range(3):
                    tmp_arr.append(board[r][2])
            board_sum_arr.append(tmp_arr)
        if rotate_direction == "+":
            board_sum_arr.rotate(-1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(1)

        for i in range(4):
            if i != 3:
                for j in range(3):
                    boards[i][j][2] = board_sum_arr[i][j]
            else:
                for j in range(3):
                    boards[i][2-j][0] = board_sum_arr[i][j]

    elif rotate_board == "U":
        board_sum_arr = deque()
        for board in boards:
            tmp_arr = []
            for c in range(3):
                tmp_arr.append(board[0][c])
            board_sum_arr.append(tmp_arr)
        if rotate_direction == "+":
            board_sum_arr.rotate(-1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(1)

        for i in range(4):
            for j in range(3):
                boards[i][0][j] = board_sum_arr[i][j]

    elif rotate_board == "D":
        board_sum_arr = deque()
        for board in boards:
            tmp_arr = []
            for c in range(3):
                tmp_arr.append(board[2][c])
            board_sum_arr.append(tmp_arr)
        if rotate_direction == "+":
            board_sum_arr.rotate(1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(-1)

        for i in range(4):
            for j in range(3):
                boards[i][2][j] = board_sum_arr[i][j]

    elif rotate_board == "F":
        board_sum_arr = deque()
        for i,board in enumerate(boards):
            tmp_arr = []
            if i == 0:
                # up
                for c in range(3):
                    tmp_arr.append(board[2][c])
            elif i == 1:
                # right
                for r in range(3):
                    tmp_arr.append(board[r][0])
            elif i == 2:
                # down
                for c in range(3):
                    tmp_arr.append((board[0][c]))
            else:
                # left
                for r in range(3):
                    tmp_arr.append((board[r][2]))

            
            board_sum_arr.append(tmp_arr)
        if rotate_direction == "+":
            board_sum_arr.rotate(1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(-1)

        if rotate_direction == "+":
            for i in range(4):
                if i == 0:
                    for j in range(3):
                        boards[i][2][2-j] = board_sum_arr[i][j]

                elif i == 1:
                    for j in range(3):
                        boards[i][j][0] = board_sum_arr[i][j]
                elif i == 2:
                    for j in range(3):
                        boards[i][0][2-j] = board_sum_arr[i][j]
                elif i == 3:
                    for j in range(3):
                        boards[i][j][2] = board_sum_arr[i][j]  
        else:
            for i in range(4):
                if i == 0:
                    for j in range(3):
                        boards[i][2][j] = board_sum_arr[i][j]
                elif i == 1:
                    for j in range(3):
                        boards[i][2-j][0] = board_sum_arr[i][j]
                elif i == 2:
                    for j in range(3):
                        boards[i][0][j] = board_sum_arr[i][j]
                elif i == 3:
                    for j in range(3):
                        boards[i][2-j][2] = board_sum_arr[i][j]


    elif rotate_board == "B":
        board_sum_arr = deque()
        for i,board in enumerate(boards):
            tmp_arr = []
            if i == 0:
                # up
                for c in range(3):
                    tmp_arr.append(board[0][c])
            elif i == 1:
                # right
                for r in range(3):
                    tmp_arr.append(board[r][2])
            elif i == 2:
                # down
                for c in range(3):
                    tmp_arr.append((board[2][c]))
            else:
                # left
                for r in range(3):
                    tmp_arr.append((board[r][0]))

            
            board_sum_arr.append(tmp_arr)

        if rotate_direction == "+":
            board_sum_arr.rotate(-1)
        elif rotate_direction == "-":
            board_sum_arr.rotate(1)

        if rotate_direction == "+":
            for i in range(4):
                if i == 0:
                    for j in range(3):
                        boards[i][0][j] = board_sum_arr[i][j]

                elif i == 1:
                    for j in range(3):
                        boards[i][2-j][2] = board_sum_arr[i][j]
                elif i == 2:
                    for j in range(3):
                        boards[i][2][j] = board_sum_arr[i][j]
                elif i == 3:
                    for j in range(3):
                        boards[i][2-j][0] = board_sum_arr[i][j]  
        else:
            for i in range(4):
                if i == 0:
                    for j in range(3):
                        boards[i][0][2-j] = board_sum_arr[i][j]
                elif i == 1:
                    for j in range(3):
                        boards[i][j][2] = board_sum_arr[i][j]
                elif i == 2:
                    for j in range(3):
                        boards[i][2][2-j] = board_sum_arr[i][j]
                elif i == 3:
                    for j in range(3):
                        boards[i][j][0] = board_sum_arr[i][j]

def rotate_itself(direction, board):
    arr = deque()
    for c in range(3):
        arr.append(board[0][c])
    for r in range(1,2):
        arr.append(board[r][2])
    for c in range(2,-1,-1):
        arr.append(board[2][c])
    for r in range(1,2):
        arr.append(board[r][0])

    if direction == "+":
        arr.rotate(2)
    elif direction == "-":
        arr.rotate(-2)

    for c in range(3):
        board[0][c] = arr.popleft()
    for r in range(1,2):
        board[r][2] = arr.popleft()
    for c in range(2,-1,-1):
        board[2][c] = arr.popleft()
    for r in range(1,2):
        board[r][0] = arr.popleft()
    
result = []
for _ in range(t):
    n = int(input())
    order = input().split()
    up = make_board("w")
    down = make_board("y")
    front = make_board("r")
    back = make_board("o")
    left = make_board("g")
    right = make_board("b")

    for direction in order:
        if direction[0] == "L" or direction[0] == "R":
            rotate([up, front, down, back], direction)
        elif direction[0] == "U" or direction[0] == "D":
            rotate([front, right, back, left], direction)
        else:
            rotate([up, right, down, left], direction)

        if direction[0] == "L":
            rotate_itself(direction[1], left)
        elif direction[0] == "R":
            rotate_itself(direction[1], right)
        elif direction[0] == "U":
            rotate_itself(direction[1], up)
        elif direction[0] == "D":
            rotate_itself(direction[1], down)
        elif direction[0] == "F":
            rotate_itself(direction[1], front)
        elif direction[0] == "B":
            rotate_itself(direction[1], back)
    for arr in up:
        result.append("".join(arr))
for r in result:
    print(r)