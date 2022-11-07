import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

# print(str1, str2)
board = [[0] * (len(str1)) for _ in range(len(str1))]


for i in range(len(str1)):
    if str1[i] == str2[0]:
        board[0][i] = 1
        for i2 in range(i+1,len(str1)):
            board[0][i2] = 1
        break

for j in range(len(str2)):
    if str2[j] == str1[0]:
        board[j][0] = 1
        for j2 in range(j+1, len(str2)):
            board[j2][0] = 1
        break


for i in range(1,len(str1)):
    check = False
    for j in range(1,len(str1)):
        if str1[j] == str2[i]:
            if not check:
    #         #     if i == 0 or j == 0:
    #         #         board[i+1][j+1] = max(board[i][j+1], board[i+1][j])
    #         #     else:
                check = True
                board[i][j] = board[i-1][j-1] + 1
        else:
            board[i][j] = max(board[i][j-1], board[i-1][j])
    #     else:
    #         board[i+1][j+1] = max(board[i][j+1], board[i+1][j])
    # # print(i,j,check)

# print(board[len(str1)-1][len(str1)-1])
print(board)

