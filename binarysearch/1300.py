import math
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())

l = 1
r = n**2

while l <= r:
    # if l == r:
    #     print(l+1)
    #     break
    mid = (l+r) // 2
    # print(mid)
    count = 0
    for i in range(1, n+1):
        count += min((mid // i),n)
    # print("count",count)
    if count >= k:
        r = mid-1
    else:
        l = mid+1
    # break
    # print(l,r,mid, count)
    # if l > r:
        # print(l)
print(l)