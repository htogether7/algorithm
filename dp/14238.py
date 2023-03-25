import sys
from collections import defaultdict
input = sys.stdin.readline
s = input().rstrip()
dp =  [[[[[""] * 3 for _ in range(3)] for _ in range(len(s)+1)] for _ in range(len(s)+1)] for _ in range(len(s)+1)]

count = defaultdict(int)
for char in s:
    count[char] += 1 
    
# a = a
# b = b
# c = c
# d = 뒤에서 두번째
# e = 뒤에서 첫번째


def dfs(a,b,c,d,e):
    if a+b+c == len(s):
        print(dp[a][b][c][d][e])
        exit(1)
        
    
    if a < count["A"] and dp[a+1][b][c][e][0] == "":
        dp[a+1][b][c][e][0] = dp[a][b][c][d][e] + "A"
        dfs(a+1,b,c,e,0)

    if b < count["B"] and e != 1 and dp[a][b+1][c][e][1] == "":
        dp[a][b+1][c][e][1] = dp[a][b][c][d][e] + "B"
        dfs(a,b+1,c,e,1)
    
    if c < count["C"] and d != 2 and e !=2 and dp[a][b][c+1][e][2] =="":
        dp[a][b][c+1][e][2] = dp[a][b][c][d][e] + "C"
        dfs(a,b,c+1,e,2)

dfs(0,0,0,0,0)
print(-1)
