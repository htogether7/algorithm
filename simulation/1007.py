import sys
import math
input = sys.stdin.readline

results = []
t = int(input())
tmp = float('inf')

def sum_vector(check,n,board):
    vector_sum = [0,0]
    for i in range(0,n,2):
        y,x = board[check[i]][check[i+1]]
        vector_sum[0] += y
        vector_sum[1] += x
    return vector_sum



def dfs(check,check_set,n,board,s):
    global tmp
    # copy_check = check[::]
    # if len(copy_check) == n:
    if len(check) == n:
        vector_sum = sum_vector(check,n,board)
        tmp = min(tmp,math.sqrt(vector_sum[0] ** 2 + vector_sum[1] ** 2))
        return

    for i in range(s,n):
        # if i in copy_check:
        if i in check_set:
            continue
        # copy_check.append(i)
        check.append(i)
        check_set.add(i)
        for j in range(n):
            if i == j:
                continue
            # if j in copy_check:
            if j in check_set:
                continue
            # copy_check.append(j)
            # dfs(copy_check,n,board)
            # copy_check.pop()
            check.append(j)
            check_set.add(j)
            dfs(check,check_set,n,board,j+1)
            check.pop()
            check_set.remove(j)
        # copy_check.pop()
        check.pop()
        check_set.remove(i)


for _ in range(t):
    check = []
    check_set = set()
    n = int(input())
    board = [[0] * (n) for _ in range(n)]
    points = [tuple(map(int,input().split())) for _ in range(n)]
    result = float('inf')

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            board[i][j] = (points[i][0] - points[j][0], points[i][1] - points[j][1])
    tmp = float('inf')
    dfs(check,check_set, n, board,0)
    results.append(tmp)

for result in results:
    print(result)

