import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
leafs = deque([])
counts = [0] * (v+1)
dict = {}
count = 0
check = [0] * (v+1)

for _ in range(v):
    arr = list(map(int,input().split()))
    if len(arr) == 4:
        leafs.append(arr[0])
        check[arr[0]] = 1
        count += 1
        counts[arr[0]] = arr[2]
    dict[arr[0]] = {}
    for i in range(1, len(arr)-1, 2):
        dict[arr[0]][arr[i]] = arr[i+1]

# print(counts)
while True:
    next_q = deque([])
    while leafs:
        next_node = leafs.popleft()
        for key in dict[next_node]:
            tmp_count = 0
            tmp_max = 0
            for child in dict[key]:
                if check[child] == 1:
                    tmp_count += 1
                    tmp_max = max(tmp_max, counts[child])
            if tmp_count == len(dict[key].keys())-1:
                next_q.append(key)
                counts[key] = tmp_max
                # check[key] = 1
                # count += 1
            else:
                next_q.append(next_node)
            # print(key)
        # print(dict[next_node])
    # if count == v:
        # break
    # print(leafs)
    print(counts)
    print(check)
    print(dict)
    break
# print(dict)
    



# print(dict)
# print(leafs)

    
