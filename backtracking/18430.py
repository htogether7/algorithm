import sys
input = sys.stdin.readline
n,m = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
dy = [[-1,0],[-1,0],[1,0],[1,0]]
dx = [[0,1],[0,-1],[0,1],[0,-1]]

def dfs(y,x,count):
    for r in range(y,n):
        for c in range(x,m):
            for i in range(4):
                if 0<=r+dy[i][0] < n and 0 <=c+dx[i][0] < m and 0 <=r+dy[i][1] < n and 0<=c+dx[i][1]<m:
                    if check[r+dy[i][0]][c+dx[i][0]] == 0 and check[r+dy[i][1]][c+dx[i][1]] == 0 and check[r][c] == 0:
                        print(r,c,count)

                # dfs()
        # dy[i]
        # dx[i]


# for i in range(n):
    # for j in range(m):
count = 0
        # print(i,j)
dfs(0,0,count)
