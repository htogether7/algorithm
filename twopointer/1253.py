import sys
input = sys.stdin.readline
n = int(input())
board = list(map(int,input().split()))

board.sort()
# print(board)
answer = 0

def check_left(i):
    if board[i] < 0:
        return False
    if i <= 1:
        return False
    
    l = 0
    r = i-1

    while l < r:
        if board[l]+board[r] == board[i]:
            return True

        if board[l]+board[r] > board[i]:
            r -= 1
        else:
            l += 1

    # while board[l] + board[r] >= board[i]:
    #     if board[l] + board[r] == board[i]:
    #         return True

    #     if r == l+1:
    #         if l != 0:
    #             l -= 1
    #             continue
    #         else:
    #             return False

        
    #     # if l == 0 and r == 1:
    #         # return False
    #     if l == 0:
    #         r -= 1
    #         continue

    #     # if abs(board[l] - board[l-1]) <= abs(board[r] - board[r-1]):
    #     #     l -= 1
    #     # else:
    #     #     r -= 1
    #     if board[l-1] + board[r] <= board[l] + board[r-1]:
    #         l -= 1
    #     else:
    #         r -= 1

    return False

def check_right(i):
    if board[i] > 0:
        return False
    if i >= len(board)-2:
        return False
    
    l = i+1
    r = len(board)-1
    
    while l < r:
        if board[l]+board[r] == board[i]:
            return True

        if board[l]+board[r] > board[i]:
            r -= 1
        else:
            l += 1
        
    # while board[l]+board[r] <= board[i]:
    #     if board[l] + board[r] == board[i]:
    #         return True
        
    #     if l == r-1:
    #         if r == len(board)-1:
    #             return False
    #         else:
    #             r += 1
    #             continue
        
    #     if r == len(board)-1:
    #         l += 1
    #         continue

    #     # if abs(board[l] - board[l+1]) >= abs(board[r] - board[r+1]):
    #         # r += 1
    #     # else:
    #         # l += 1
    #     if board[l]+board[r+1] > board[l+1]+board[r]:
    #         r += 1
    #     else:
    #         l += 1
    return False

def check_both(i):
    if i == 0 or i == len(board)-1:
        return False
    
    l = 0
    r = len(board)-1
    while l < i and r > i:
        if board[l] + board[r] == board[i]:
            return True
        
        if l == i-1 and r == i+1:
            return False

        if l == i-1:
            r -= 1
            continue
        
        if r == i +1:
            l += 1
            continue

        # if abs(board[i]-(board[r-1]+board[l])) > abs(board[i]-(board[l+1]+board[r])):
        #     r -= 1
            
        # else:
        #     l += 1
        if board[l]+board[r] < board[i]:
            l += 1
        else:
            r -= 1
    return False

answer = 0
for i in range(len(board)):
    if check_both(i):
        answer += 1
        # print(i)
        continue

    if check_left(i):
        answer += 1
        # print(i)
        continue

    if check_right(i):
        answer += 1
        # print(i)
        continue

#     if i <= 1:
#         continue



print(answer)