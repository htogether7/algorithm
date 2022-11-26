import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = []
answer = []
# check = [0] * (n+1)

def dfs(s):
    if len(arr) == m:
        answer.append(arr[::])
        return
    if s == n+1:
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i)
            arr.pop()

dfs(1)
# print(answer)
for a in answer:
    print(" ".join(list(map(str, a))))