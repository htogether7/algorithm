from collections import deque

from numpy import Infinity;
n,m = map(int,input().split());

arr = [];
for i in range(n):
    arr.append(list(map(int,input())));
# print(arr);

checked = [m*[0] for i in range(n)];
# print(checked);

queue = deque();
queue.append([0,0, 1]);
checked[0][0] = 1;

dx = [0,0,1,-1];
dy = [1,-1,0,0];

min_result = Infinity;
while queue:
    next = queue.popleft();
    # print(next);
    if next[0] == n-1 and next[1] == m-1:
        min_result = min(min_result, next[2]);
    for i in range(4):
        if next[0] + dy[i] >= 0 and next[0] + dy[i] < n and next[1] + dx[i] >= 0 and next[1] + dx[i] < m and arr[next[0]+dy[i]][next[1]+dx[i]] == 1 and checked[next[0]+dy[i]][next[1]+dx[i]] == 0:
            queue.append([next[0]+dy[i], next[1]+dx[i], next[2]+1]);
            checked[next[0]+dy[i]][next[1]+dx[i]] = 1;
    # print(queue);
print(min_result);
