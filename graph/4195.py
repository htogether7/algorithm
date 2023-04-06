import sys
input = sys.stdin.readline

t = int(input())

def find(x, parents):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x,y, parents, counts):
    X = find(x, parents)
    Y = find(y, parents)
    if X == Y:
        return
    elif X < Y:
        parents[Y] = X
        counts[X] += counts[Y]
    else:
        parents[X] = Y
        counts[Y] += counts[X]

def is_union(x,y, parents):
    X = find(x, parents)
    Y = find(y, parents)
    if X == Y:
        return True
    else:
        return False


answer = []

for i in range(t):
    parents = {}
    count_dict = {}
    f = int(input())
    for j in range(f):
        a,b = input().split()
        if a not in parents:
            parents[a] = a
            count_dict[a] = 1
        
        if b not in parents:
            parents[b] = b
            count_dict[b] = 1

        if not is_union(a,b, parents):
            union(a,b, parents,count_dict)

        root = find(a,parents)
        answer.append(count_dict[root])

for a in answer:
    print(a)
