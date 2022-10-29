import sys
input = sys.stdin.readline

n = int(input())

board = list(map(int, input().split()))
board.sort()

if board[0] <= 0 and board[-1] <= 0:
    print(board[-2], board[-1])
elif board[0] >= 0 and board[-1] >= 0:
    print(board[0], board[1])
else:
    l = 0
    r = n-1
    answer = [board[l], board[r], board[l]+board[r]]
    while l < r:
        if l + 1 == r:
            break
        left_tmp = board[l+1] + board[r]
        right_tmp = board[l] + board[r-1]

        if abs(left_tmp) <= abs(right_tmp):
            l += 1
        else:
            r -= 1
        
        if abs(board[l]+board[r]) < abs(answer[2]):
            answer[0] = board[l]
            answer[1] = board[r]
            answer[2] = board[l]+board[r]
    print(answer[0], answer[1])
# print(board)