import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

def cal_min_value(x,y,d1,d2):
    check = [[-1] * n for _ in range(n)]
    up = (x,y)
    left = (x+d1, y-d1)
    down = (x+d1+d2, y-d1+d2)
    right = (x+d2, y+d2)

    one = 0
    two = 0
    three = 0
    four = 0
    five = 0

    # 구역 1
    for i in range(x+d1):
        if i < up[0]:
            for j in range(up[1]+1):
                
                one += board[i][j]
                check[i][j] = 1
        else:
            for j in range(up[1]+up[0]-i):
                one += board[i][j]
                check[i][j] = 1

    # 구역 2
    for i in range(x+d2+1):
        if i < up[0]:
            for j in range(up[1]+1, n):
                two += board[i][j]
                check[i][j] = 2
        else:
            for j in range(up[1]+i-up[0]+1,n):
                two += board[i][j]
                check[i][j] = 2
    
    # 구역 3
    for i in range(x+d1,n):
        if i > x+d1+d2:
            for j in range(y-d1+d2):
                three += board[i][j]
                check[i][j] = 3
        else:
            for j in range(i-left[0]+left[1]):
                three += board[i][j]
                check[i][j] = 3

    # 구역 4
    for i in range(x+d2+1, n):
        if i > x+d1+d2:
            for j in range(y-d1+d2,n):
                four += board[i][j]
                check[i][j] = 4
        else:
            for j in range(right[1] + right[0]-i+1, n):
                four += board[i][j]
                check[i][j] = 4

    # 구역 5
    for i in range(n):
        for j in range(n):
            if check[i][j] == -1:
                five += board[i][j]

    sums = [one,two,three,four,five]

    return max(sums) - min(sums)

answer = float('inf')
for x in range(n):
    for y in range(n):
        for d1 in range(1,n):
            for d2 in range(1,n):
                if x+d1+d2 >= n:
                    continue
                if y-d1 < 0 or y+d2 >= n:
                    continue
                answer = min(answer, cal_min_value(x,y,d1,d2))

print(answer)

