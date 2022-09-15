import sys;
from collections import deque;
input = sys.stdin.readline;

n,m,t = map(int, input().split());
board = [list(map(int,input().split())) for _ in range(n)];

check = [[0] * m for _ in range(n)];
check[0][0] = 1;

q = deque([]);
q.append([0,0,0]);

dx = [1,-1,0,0];
dy = [0,0,1,-1];

done = False;
answer = 10000;

while q:
    
    if done: 
        break;
    y,x,time = q.popleft();
    if board[y][x] == 1:
        continue;
    if time > t:
        break;
    board[y][x] = 1;
    for i in range(4):
        # print(board);
        if 0<=y+dy[i] < n and 0 <= x+dx[i] < m:
            
            if board[y+dy[i]][x+dx[i]] == 0:
                if y+dy[i] == n-1 and x+dx[i] == m-1:
                    # print(time+1);
                    if time + 1 <= t:
                        answer = min(answer, time+1)
                        done = True;
                        break;
                    else:
                        break;
                q.append([y+dy[i], x+dx[i], time+1]);
                
            elif board[y+dy[i]][x+dx[i]] == 2:
                if time+1+ (m-1) - (x+dx[i]) + (n-1) - (y+dy[i]) <= t:
                    answer = min(answer, time+1+ (m-1) - (x+dx[i]) + (n-1) - (y+dy[i]))
                # print();
                    done = True;
                # break;
    # print(board);
if not done:
    print("Fail")
else:
    print(answer);
# print(board);
