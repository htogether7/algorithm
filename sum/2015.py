import sys;
from collections import deque;
input = sys.stdin.readline;
n, k = map(int, input().split());
arr = list(map(int, input().split()));
answer = 0;
# sum = [0];
# tmp = 0;
# answer = 0;
# for i in arr:
#     tmp += i;
#     sum.append(tmp);
# for i in range(1,len(sum)):
#     for j in range(0,i):
#         if sum[i]-sum[j] == k:
#             answer += 1;
# print(answer);
map = {};
for i in arr:
    tmp = {};
    if len(map) == 0:
        tmp[i] = 1;
        map = tmp;
    else:
        for j in map:
            if j + i == k:
                answer+=map[j];
            
            if i+j not in tmp:
                tmp[i+j] = map[j];
            else:
                tmp[i+j] += map[j];
        if i in tmp:
            tmp[i] += 1;
        else:
            tmp[i] = 1;
        if i == k:
            answer += 1;
        # print(tmp);
        # print(answer);
        map = tmp;
        # map.append(tmp);
        # map.popleft();
# print(map);
print(answer);


# print(sum);