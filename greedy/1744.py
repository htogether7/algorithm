import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
board = [int(input().rstrip()) for _ in range(n)]
board.sort()

minus = deque()
zero = deque()
plus = deque()
for num in board:
    if num == 0:
        zero.append(num)
    elif num < 0:
        minus.append(num)
    else:
        plus.append(num)

# print(minus)
# print(zero)
# print(plus)

answer = 0
minus_index = 0
# if len(minus) > 1:
while len(minus) > 1:
    
    # minus_index += 2
    a = minus.popleft()
    b = minus.popleft()
    answer += a*b

# if len(minus) >= 1 and len(zero) >= 1:
while len(minus) >= 1 and len(zero) >= 1:
    minus.popleft()
    zero.popleft()
# print(minus)
# print(minus + plus)

board = minus + zero + plus
# print(answer)
# print(board)

# zero_count = 

index = len(board)-1
# answer = 0
tmp = 0
while index > 0:
    if board[index] * board[index-1] > board[index] + board[index-1]:
        tmp += board[index] * board[index-1]
    else:
        tmp += (board[index] + board[index-1])

    index -= 2
    # print(index, answer)
if index == 0:
    tmp += board[0]
answer += tmp
print(answer)
# answer = tmp

# index = 0
# tmp = 0
# while index < len(board)-1:
#     if board[index] * board[index+1] > board[index] + board[index+1]:
#         tmp += board[index] * board[index+1]
#     else:
#         tmp += (board[index] + board[index+1])

#     index += 2
# if index == len(board)-1:
#     tmp += board[index]
# # print(tmp)
# answer = max(tmp, answer)
# print(answer)
# # print(board)