import sys
input = sys.stdin.readline
n = int(input())

paris = list(map(int,input().split()))
# paris = [i+1 for i in range(40000)]
board = [40001] * (n+1)

def bs(board,target):
    s_index = 0
    e_index = len(board)
    while s_index <= e_index:
        mid_index = (s_index + e_index) // 2
        
        if board[mid_index] < target:
            s_index = mid_index+1
        else:
            e_index = mid_index-1
    return s_index


for num in paris:
    board[bs(board,num)] = num
    # print(board)
# print(board)
for i in range(len(board)):
    if board[i] == 40001:
        print(i)
        break