import sys
input = sys.stdin.readline

n,k = map(int, input().split())
fishes = [list(map(int,input().split()))]



def max_difference(arr):
    return max(arr[0]) - min(arr[0])

def add_fish(arr):
    min_value = min(arr[0])
    for i in range(len(arr[0])):
        if arr[0][i] == min_value:
            arr[0][i] += 1

def check_rotation_possible(board):
    if len(board) == 1:
        return True
    floor_legnth = 0
    for i in range(len(board[0])):
        if board[0][i] == 0:
            floor_legnth = len(board[0]) - i
            break
    if len(board) > floor_legnth:
        return False
    else:
        return True
    
def rotate(board):
    if len(board) == 1:
        new_board = [[0] * (len(board[0])-1) for _ in range(2)]
        new_board[0][0] = board[0][0]
        for i in range(1,len(board[0])):
            new_board[1][i-1] = board[0][i]
        return new_board
    
    else:
        height = 0
        for i in range(len(board[0])):
            if board[0][i] == 0:
                height = i
                break

        new_board = [[0] * (len(board[0]) - height) for _ in range(height+1)]

        for r in range(len(board)):
            for c in range(height):
                # if height == 1:
                    # new_board[c][height-r] = board[r][c]
                # else:
                new_board[c][len(board)-1-r] = board[r][c]

        for c in range(height, len(board[0])):
            new_board[-1][c-height] = board[-1][c]

        return new_board
    


def divide_fish(fishes):
    h = len(fishes)
    w = len(fishes[0])
    # print(h,w)
    count_board = [[0] * w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            if r != 0 and (fishes[r-1][c] != 0 and fishes[r][c] != 0):
                div = abs(fishes[r][c] - fishes[r-1][c]) // 5
                # print(div)
                # if div <= 0:
                    # continue

                if fishes[r][c] < fishes[r-1][c]:
                    count_board[r][c] += div
                    count_board[r-1][c] -= div
                else:
                    count_board[r][c] -= div
                    count_board[r-1][c] += div
                # print(count_board)
            # if fishes[r][c+1] == 0:
            #     break
            if c != w-1 and fishes[r][c+1] != 0:
                div = abs(fishes[r][c] - fishes[r][c+1]) // 5
                # # if div <= 0:
                #     # continue

                if fishes[r][c] < fishes[r][c+1]:
                    count_board[r][c] += div
                    count_board[r][c+1] -= div
                else:
                    count_board[r][c] -= div
                    count_board[r][c+1] += div
            # print(r,c,count_board)
    # print(fishes)
    # print(count_board)
    for r in range(h):
        for c in range(w):
            fishes[r][c] += count_board[r][c]

def flat(fishes):
    arr = []
    for c in range(len(fishes[0])):
        for r in range(len(fishes)-1,-1,-1):
            if fishes[r][c] != 0:
                arr.append(fishes[r][c])
    return [arr]

def fold(fishes):
    half = len(fishes[0]) // 2
    new_board = [[0] * (half) for _ in range(2)]
    for i in range(half):
        new_board[0][half-1-i] = fishes[0][i]
    for i in range(half, len(fishes[0])):
        # print(i, half)
        new_board[1][i-half] = fishes[0][i]
        # print(new_board)
    
    quarter = half // 2
    result = [[0] * quarter for _ in range(4)]
    for r in range(2):
        for c in range(quarter):
            result[1-r][quarter-1-c] = new_board[r][c]

    for r in range(2):
        for c in range(quarter, len(new_board[0])):
            result[2+r][c-quarter] = new_board[r][c]
    return result
    # result = []

count = 0
while True:
    if max_difference(fishes) <= k:
        print(count)
        break

    add_fish(fishes)
    while check_rotation_possible(fishes):
        fishes = rotate(fishes)
        # print(fishes)
    # break
    divide_fish(fishes)
    fishes = flat(fishes)
    # print(fishes)
    fishes = fold(fishes)
    divide_fish(fishes)
    fishes = flat(fishes)
    
    # break



    count += 1