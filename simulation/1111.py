import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int,input().split()))

tmp = []
answer = []

if n == 1:
    print("A")
elif n == 2:
    if board[0] == board[1]:
        print(board[0])
    else:
        print("A")
else:
    if board[0] == board[1]:
        a = 0
    else:
        a = (board[2] - board[1]) // (board[1] - board[0])

    b = board[1] - a * board[0]
    for i in range(2, n):
        if board[i] != board[i-1] * a + b:
            break
        if i == n-1:
            answer.append(board[-1] * a + b)

    if len(answer) == 0:
        print("B")
    elif len(answer) > 1:
        print("A")
    else:
        print(answer[0])
