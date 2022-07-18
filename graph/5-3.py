from collections import deque;
n,m = map(int, input().split());
arr = [];
for i in range(n):
    arr.append(list(map(int,input())));

result = 0;
# def bfs()

dx = [0,0,1,-1];
dy = [1,-1,0,0];

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
           result += 1;
           queue = deque();
           queue.append([i,j]);
           arr[i][j] = 1;
           while queue:
            next = queue.popleft();
            for k in range(4):
                # if arr[next[0] + dx[k]][next[1] + dy[k]] and  arr[next[0] + dx[k]][next[1] + dy[k]] == 0:
                if next[0] + dx[k] >= 0 and next[0] + dx[k] < n and next[1] + dy[k] >= 0 and next[1] + dy[k] < m and  arr[next[0] + dx[k]][next[1] + dy[k]] == 0:
                    queue.append([next[0] + dx[k], next[1] + dy[k]]);
                    arr[next[0] + dx[k]][next[1] + dy[k]] = 1;
print(result);

