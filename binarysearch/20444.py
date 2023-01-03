import sys
input = sys.stdin.readline

n,k = map(int, input().split())

r = n
l = 0

checkPossible = False
while l <= r:
    mid = (l+r) // 2
    num = (mid+1) * (n-mid+1)
    if num == k:
        checkPossible = True
        break
    elif num > k:
        l = mid+1
    else:
        r = mid -1

if checkPossible:
    print("YES")
else:
    print("NO")
