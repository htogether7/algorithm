import sys
input = sys.stdin.readline

n = int(input())
board = list(map(int,input().split()))
dp = [board[0]]
answer = 0

def bs(dp, target):
    s = 0;
    e = len(dp)-1

    while s <= e:
        mid = (s+e) // 2
        if dp[mid] == target:
            return mid
        elif dp[mid]< target:
            s = mid+1
        else:
            e = mid-1
    return s
            

        



for i in range(n):
    # if not dp:
    #     dp.append(board[i])
    # else:
    if board[i] > dp[-1]:
        dp.append(board[i])
    else:
        dp[bs(dp, board[i])] = board[i]
        
    # if board[i]> dp[i]:
    # print(dp)

print(len(dp))
# print(dp)

# print(board)