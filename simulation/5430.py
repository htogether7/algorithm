import sys
input = sys.stdin.readline

t = int(input())
result = []
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = input()
    arr = arr[1:-2]
    q = None
    if not arr:
        q = list()
    else:
        q = list(map(int,arr.split(",")))
    flag = 0
    l = 0
    r = n-1
    error = False
    # flag 0이면 왼쪽, 1이면 오른쪽
    for f in p:
        if f == "R":
            flag = abs(1-flag)
        else:
            if flag == 0:
                l+=1
            else:
                r-=1
            if r < l and abs(r-l) > 1:
                error = True
                break
    if error:
        result.append("error")
    else:
        tmp = q[l:r+1]
        if flag == 1:
            tmp.reverse()
        content = ""
        if tmp:
            content = ",".join(map(str,tmp))
        tmp = "[" + content + "]"
        result.append(tmp)

for r in result:
    print(r)