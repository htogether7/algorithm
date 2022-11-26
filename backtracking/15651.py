import sys
input = sys.stdin.readline

n,m = map(int, input().split())
answer = []
arr = []
def dfs(s):
    if len(arr) == m:
        answer.append(arr[::])
        return
    
    for i in range(1,n+1):
        arr.append(i)
        dfs(i)
        arr.pop()
dfs(0)
for a in answer:
    print(" ".join(map(str,a)))