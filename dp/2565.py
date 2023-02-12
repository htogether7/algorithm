import sys
input = sys.stdin.readline

n = int(input())
dict = {}
for _ in range(n):
    a,b = map(int, input().split())
    dict[a] = b
# board = [list(map(int,input().split())) for _ in range(n)]
# board.sort(key = lambda x : x[0])
# print(dict)

dp = [[0] * (501) for _ in range(101)]
for j in range(1,501):
    if j not in dict:
        for row in range(1,101):
            dp[row][j] = dp[row][j-1]
        continue
    for i in range(1, 101):
        if i == 1:
            if dp[i][j-1] == 0:
                dp[i][j] = dict[j]
            else:
                dp[i][j] = min(dict[j], dp[i][j-1])
        else:
            if dp[i-1][j-1] != 0 and dict[j] > dp[i-1][j-1]:
                if dp[i][j-1] == 0:
                    dp[i][j] = dict[j]
                else:
                    dp[i][j] = min(dict[j], dp[i][j-1])
            else:
                dp[i][j] = dp[i][j-1]
    # break
# print([dp[i][:7] for i in range(7)])
# for (a,b) in board:
answer = 0
def find():
    global answer;
    for row in range(100, -1,-1):
        for c in range(501):
            if dp[row][c] != 0:
                answer = row
                # print(answer)
                return
find()

print(n-answer)

# print(dp)
# print(board)
# print(board)