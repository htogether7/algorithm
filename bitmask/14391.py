import sys
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

# while 
arr = []
answer = 0

def mask(arr):
    global answer
    tmp_result = 0
    check_board = [[0]*m for i in range(n)]
    for r in range(len(arr)):
        s = arr[r][0]
        e = arr[r][1]
        tmp = ''
        for c in range(s,e):
            check_board[r][c] = 1
            tmp += board[r][c]
        if len(tmp) > 0:
            tmp_result += int(tmp)
        # print(s,e)
        # print(tmp)
        # for 
    # print(check_board)
    for r in range(n):
        for c in range(m):
            if check_board[r][c] == 0:
                now_row = r
                tmp = ''
                while now_row < n and check_board[now_row][c] == 0:
                    tmp += board[now_row][c]
                    check_board[now_row][c] = 1
                    now_row += 1
                if len(tmp) > 0:
                    tmp_result += int(tmp)
    answer = max(answer, tmp_result)
    # print(tmp_result)
        # copy_board[r]
        # copy_board[r][section[0]:section[1]]

def dfs(l):
    if l == n:
        # print(arr)
        mask(arr)
        return

    for i in range(m+1):
        for j in range(i,m+1):
            arr.append((i,j))
            dfs(l+1)
            arr.pop()
dfs(0)
print(answer)
# if n > m:
#     result = 0
#     for c in range(m):
#         str_num = ''
#         for r in range(n):
#             str_num += board[r][c]
#         # print(str_num)
#         result += int(str_num)
#     print(result)
# elif n < m:
#     result = 0
#     for r in range(n):
#         str_num = ''
#         for c in range(m):
#             str_num += board[r][c]
#         # print(str_num)
#         result += int(str_num)
#     print(result)
# else:
    # pass
# print(board)
