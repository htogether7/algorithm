import sys
from collections import deque
input = sys.stdin.readline

n,m,k = map(int,input().split())
count = 0

def nCr(a,z):
    num = 1
    for i in range(a+z,a,-1):
        num *= i
    for i in range(z,1,-1):
        num = num // i
    return num

dp = {}

def dfs(a,z,s,c):
    global count
    # print(a,z)
    
    if a != 0:
        tmp_count = nCr(a,z)
        print(tmp_count, a,z)
        if tmp_count + c == k:
            # z앞에 다 채우고 그다음에 a채우기
            print(s + "z" * z + "a" * a )
            exit(1)
        elif tmp_count + c > k:
            dfs(a-1,z,s+"a",c)
        else:
            dp[s] = tmp_count+c
            # dfs()

    if z != 0:
        if s in dp:
            tmp_count = dp[s]
            # print(tmp_count)
            if tmp_count + c == k:
                print(s+"z" * z + "a" * a)
                exit(1)
            elif tmp_count + c > k:
                dfs(a,z-1,s+"z",c)
        
    # if a == 0 and z == 0:
    #     count += 1
    #     print(s)
    #     if count == k:
    #         print(s)
    #         exit(1)
    #     return
    
    # if a != 0:
    #     dfs(a-1,z,s+"a")
    # if z != 0:
    #     dfs(a,z-1,s+"z")


if nCr(n,m) < k:
    print(-1)
else:
    dfs(n,m,"",0)
print(dp)