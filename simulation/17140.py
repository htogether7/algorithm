import sys
from collections import defaultdict
input = sys.stdin.readline

r,c,k = map(int, input().split())
board = [list(map(int,input().split())) for _ in range(3)]

def row_sort(board):
    max_length = 0
    new_board = []
    for row in range(len(board)):
        tmp_dict = defaultdict(int)
        for col in range(len(board[0])):
            if board[row][col] == 0:
                continue
            tmp_dict[board[row][col]] += 1
        items = list(tmp_dict.items())
        items.sort(key = lambda x: (x[1], x[0]))

        tmp_arr = []
        for key, count in items:
            tmp_arr.append(key)
            tmp_arr.append(count)
            if len(tmp_arr) == 100:
                break
        max_length = max(max_length, len(tmp_arr))
        new_board.append(tmp_arr)
    for arr in new_board:
        for _ in range(max_length - len(arr)):
            arr.append(0)
    return new_board


def col_sort(board):
    max_length = 0
    new_board = []
    for col in range(len(board[0])):
        tmp_dict = defaultdict(int)
        for row in range(len(board)):
            if board[row][col] == 0:
                continue
            tmp_dict[board[row][col]] += 1
        items = list(tmp_dict.items())
        items.sort(key = lambda x: (x[1], x[0]))
        tmp_arr = []
        for key, count in items:
            tmp_arr.append(key)
            tmp_arr.append(count)
            if len(tmp_arr) == 100:
                break
        max_length = max(max_length, len(tmp_arr))
        new_board.append(tmp_arr)
    for arr in new_board:
        for _ in range(max_length - len(arr)):
            arr.append(0)
    # print(new_board)
    rotated_new_board = [[0] * len(new_board) for _ in range(len(new_board[0]))]
    for i in range(len(new_board)):
        for j in range(len(new_board[0])):
            rotated_new_board[j][i] = new_board[i][j]
    # print(rotated_new_board)
    return rotated_new_board


def two_dimension_sort(board):
    count = 0
    while count <= 100:
        if r-1 < len(board) and c-1 < len(board[0]) and board[r-1][c-1] == k:
            return count
        h = len(board)
        w = len(board[0])

        if h >= w:
            board = row_sort(board)
        else:
            board = col_sort(board)
    
        count += 1

    return -1

# col_sort(board)
print(two_dimension_sort(board))