import sys
from collections import deque
input = sys.stdin.readline
n = int(input())


def make_queue():
    q = deque([])
    for i in range(n):
        arr = list(map(int,input().split()))
        time = arr[0] 
        prerequistes = arr[1:-1]
        q.append((i+1, time, prerequistes))
    return q

q = make_queue()

dp = [0] * (n+1)

def find_max_of_prerequistes(prerequistes):
    tmp = -1
    for i in prerequistes:
        if dp[i] == 0:
            return 0
        tmp = max(tmp, dp[i])
    return tmp


while q:
    index, time, prerequistes = q.popleft()
    max_of_prerequistes = find_max_of_prerequistes(prerequistes)
    if max_of_prerequistes == 0:
        q.append((index,time,prerequistes))
    elif max_of_prerequistes == -1:
        dp[index] = time
    else:
        dp[index] = max_of_prerequistes + time

for i in range(1,n+1):
    print(dp[i])