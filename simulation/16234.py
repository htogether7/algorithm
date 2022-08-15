import sys;
from collections import defaultdict;
from collections import deque;
input = sys.stdin.readline;
n, l, r = map(int, input().split())
sys.setrecursionlimit(10**6)

board = [list(map(int, input().split())) for _ in range(n)];

checked = [[0]*n for _ in range(n)];
count = 1;

dx = [1, -1, 0, 0];
dy = [0, 0, 1, -1];

def dfs(i,j):
    for k in range(4):
        if 0 <= i+dy[k] < n and 0 <= j+dx[k] < n and checked[i+dy[k]][j+dx[k]] == 0 and l <= abs(board[i][j]-board[i+dy[k]][j+dx[k]]) <= r:
            checked[i+dy[k]][j+dx[k]] = count;
            dict[count]+= board[i+dy[k]][j+dx[k]];
            count_dict[count] += 1;
            dfs(i+dy[k],j+dx[k]);

counter = 0;
while True:
    # if counter == 1:
        # break;
    dict = defaultdict(int);
    count_dict = defaultdict(int);
    count = 1;
    for i in range(n):
        for j in range(n):
            if checked[i][j] == 0:
                q = deque([]);
                q.append([i,j]);
                checked[i][j] = count;
                while q:
                    [row,col] = q.popleft();
                    # print(row,col);
                    for k in range(4):
                        if 0 <= row+dy[k] < n and 0 <= col+dx[k] < n and checked[row+dy[k]][col+dx[k]] == 0 and l <= abs(board[row][col]-board[row+dy[k]][col+dx[k]]) <= r:
                            checked[row+dy[k]][col+dx[k]] = count;
                            dict[count]+= board[row+dy[k]][col+dx[k]];
                            count_dict[count] += 1;
                            q.append([row+dy[k], col+dx[k]]);
                    
                count += 1;
            # if checked[i][j] == 0:
            #     checked[i][j] = count;
            #     dict[count] += board[i][j];
            #     count_dict[count] += 1;
            #     dfs(i,j);
            #     count+=1;
    # print(checked);
    # print(dict);
    # print(count_dict);
    if checked[n-1][n-1] == n**2:
        break;
    for i in range(n):
        for j in range(n):
            board[i][j] = dict[checked[i][j]] // count_dict[checked[i][j]];
    # print(checked);
    # print(board);

    counter += 1;

    checked = [[0]*n for _ in range(n)];

    
print(counter);
# print(dict);
# print(count_dict);

# print(board);


