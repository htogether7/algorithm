import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
dict = defaultdict(list)
levels = [0] * 10001
level_dict = defaultdict(list)
level_dict[0].append(1)
max_level = 0
maxs = [0] * 10001
answer = 0

for _ in range(n-1):
    parent,child,weight = map(int,input().split())
    if levels[child] == 0:
        levels[child] = levels[parent] + 1
        level_dict[levels[child]].append(child)
        max_level = max(max_level, levels[child])

    # print(input().split())
    dict[parent].append((weight, child))
# print(max_level)

for level in range(max_level-1, -1, -1):
    # print(level_dict[level])
    for parent_node in level_dict[level]:
        # max_node = (-1,0)
        max_weight = []
        # dict[parent_node]
        for w, child in dict[parent_node]:
            # if w+maxs[child] > max_node[1]:
            max_weight.append(w+maxs[child])
            maxs[parent_node] = max(maxs[parent_node], w+maxs[child])
        max_weight.sort(reverse=True)
        if len(max_weight) >= 2:
            answer = max(answer, max_weight[0]+max_weight[1])
        # print(max_weight)
# print(max(maxs))
# print(level_dict)
# print(dict)
answer = max(answer, max(maxs))
print(answer)