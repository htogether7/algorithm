import sys
from collections import defaultdict
input = sys.stdin.readline

n,k = map(int, input().split())

dp = [[[[""] * int((n * (n-1) / 2)+1) for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]

#a = A개수
#b = B개수
#c = C개수
#d = 증가하는 쌍의 개수 

def count_increase(str):
    count = 0
    for i in range(len(str)-1):
        for j in range(i+1):
            if str[i] < str[j]:
                count += 1
    return count


def dfs(a,b,c,d):
    if a+b+c == n and d == k:
        print(dp[a][b][c][d])
        exit(0)
    
    if a+b+c >= n:
        return
    
    if a < n and dp[a+1][b][c][d] == "":
        dp[a+1][b][c][d] = dp[a][b][c][d] + "A"
        dfs(a+1,b,c,d)
    
    if b < n and dp[a][b+1][c][d+a] == "":
        dp[a][b+1][c][d+a] = dp[a][b][c][d] + "B"
        dfs(a,b+1,c,d+a)

    if c < n and dp[a][b][c+1][d+a+b] == "":
        dp[a][b][c+1][d+a+b] = dp[a][b][c][d] + "C"
        dfs(a,b,c+1,d+a+b)

dfs(0,0,0,0)
print(-1)