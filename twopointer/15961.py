import sys;
# from collections import deque;
from collections import defaultdict
input = sys.stdin.readline;
n, d, k, c = map(int, input().split());

sushi = [];

for _ in range(n):
    sushi.append(int(input()));

sushi = sushi * 2;
# count = 0;
sushi_sort = defaultdict(int);
for i in range(0,k):
    # if sushi[i] in sushi_sort:
    #     sushi_sort[sushi[i]] += 1;
    # else:
    #     sushi_sort[sushi[i]] = 1;
    sushi_sort[sushi[i]] += 1;
sushi_sort[c] += 1;

max_sushi = len(sushi_sort.keys());
# add = False;
# if c not in sushi_sort.keys():
#     add = True;

l = 0;
r = k;
while l < n:
    sushi_sort[sushi[l]] -= 1;
    if sushi_sort[sushi[l]] == 0:
        del sushi_sort[sushi[l]];
        # if sushi[l] == c:
        #     add = True;
    # if sushi[r] in sushi_sort:
    #     sushi_sort[sushi[r]] += 1;
    # else:
    #     sushi_sort[sushi[r]] = 1;
    sushi_sort[sushi[r]] += 1;
    # if sushi[r] == c:
    #     add = False;
    # if add == False:
    max_sushi = max(max_sushi, len(sushi_sort.keys()));
    # else:
        # max_sushi = max(max_sushi, len(sushi_sort.keys()) + 1);
    l += 1;
    r += 1;
    # count += 1;
    # sushi.append(sushi.popleft());
    # print(sushi_sort);
print(max_sushi);

# print(n,d,k,c);