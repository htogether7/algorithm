import sys
input = sys.stdin.readline

l,c = map(int, input().split())
chars = list(input().split())

moum = []
jaum = []

for char in chars:
    if char in ["a", "e", "i", "o", "u"]:
        moum.append(char)
    else:
        jaum.append(char)

moum.sort()
jaum.sort()

result = []

moum_combinations = []
jaum_combinations = []

tmp = []

def dfs(l,s,r,arr):
    global tmp
    if l == r:
        if arr == moum:
            moum_combinations.append(tmp[::])
        elif arr == jaum:
            jaum_combinations.append(tmp[::])

        # print(tmp)
        return
    
    for i in range(s, len(arr)):
        tmp.append(arr[i])
        dfs(l+1,i+1,r,arr)
        tmp.pop()
        

for r in range(2,len(jaum)+1):
    dfs(0,0,r,jaum)

for r in range(1,len(moum)+1):
    dfs(0,0,r,moum)


for j in jaum_combinations:
    for m in moum_combinations:
        if len(j+m) == l:
            j_plus_m = j+m
            j_plus_m.sort()
            result.append("".join(j_plus_m))

result.sort()

for r in result:
    print(r)