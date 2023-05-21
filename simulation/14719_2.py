import sys
input = sys.stdin.readline
h,w = map(int, input().split())
board = list(map(int,input().split()))


# O(n^2) 풀이
answer = 0
board = [0] + board + [0]
for i in range(1, w+1):
    max_height = min(max(board[:i]), max(board[i+1:]))
    if max_height > board[i]:
        answer +=  (max_height - board[i])
print(answer)


# water[i] = min(left_max, right) - board[i]


# O(n) 풀이

max_index = 0
for i in range(w):
    if board[i] > board[max_index]:
        max_index = i

answer = 0

left = 0
right = len(board)-1

left_max = 0
while left < max_index:
    if left_max <= board[left]:
        left_max = board[left]
    else:
        answer += (left_max - board[left])

    left += 1

right_max = 0
while right > max_index:
    if right_max <= board[right]:
        right_max = board[right]
    else:
        answer += (right_max - board[right])
    right -= 1

print(answer)