import sys
from collections import defaultdict, deque
input = sys.stdin.readline

k = int(input())
# graph = []
result = []
for _ in range(k):
    v,e = map(int, input().split())

    dict = defaultdict(list)
    for _ in range(e):
        a,b = map(int,input().split())
        dict[a].append(b)
        dict[b].append(a)

    check = [0] * (v+1)
    # start = list(dict.keys())[0]
    # check[start] = 1
    # q = deque([])
    # q.append((start,1))
    check_possible = True

    if v == 1:
        check_possible = False

    for start in list(dict.keys()):
        q = deque([])
        if check[start] == 0:
            check[start] = 1
            q.append((start,1))
        else:
            q.append((start,check[start]))
        
        # check_possible = True
        while q:
            next, color = q.popleft()
            stop_while = False
            # print(check,q)
            for node in dict[next]:
                if check[node] == 0:
                    q.append((node, 3-color))
                    check[node] = 3-color
                elif check[node] == 1:
                    if color == 1:
                        if node != next:

                            check_possible = False
                            stop_while = True
                            break
                elif check[node] == 2:
                    if color == 2:
                        if node != next:
                            check_possible = False
                            stop_while = True
                            break
            # print(check,q)
            if stop_while:
                break



    if check_possible:
        result.append("YES")
    else:
        result.append("NO")
        # dict[next]
    # print(start)
    # graph.append(dict)
for i in result:
    print(i)

# print(graph)

