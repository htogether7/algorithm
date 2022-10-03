import sys;
from collections import deque;
import math;
input = sys.stdin.readline;
sys.setrecursionlimit(10**5)
answer = 0;
n,left,right = map(int, input().split());
board = [list(map(int,input().split())) for _ in range(n)];
check = [[0] * n for _ in range(n)];
count = 0;

while True:
    count += 1;
    q_count = 0;
    for r in range(n):
        for c in range(n):
            
            
            if check[r][c] != count:
                print(check, r, c);
                sum = 0;
                ter_count = 0;
                ter_arr = [];
                # print(check);
                q = deque([[r,c,board[r][c]]]);
                check[r][c] = count;
                while q:
                    
                    now_r, now_c, now_pop = q.popleft();
                    ter_arr.append([now_r,now_c]);
                    sum += now_pop;
                    ter_count += 1;        
                    for dy,dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                        if 0<=now_r+dy<n and 0<=now_c+dx<n and check[now_r+dy][now_c+dx] != count and left <= abs(board[now_r+dy][now_c+dx] - now_pop) <= right: 
                            q.append([now_r+dy,now_c+dx,board[now_r+dy][now_c+dx]]);
                            check[now_r+dy][now_c+dx] = count;
                            q_count +=1;
                            # print(check);
                            # print(q);
                pop_result = sum // ter_count;
                # print(pop_result, sum, ter_count, ter_arr);
                for row,col in ter_arr:
                    board[row][col] = pop_result;
                # all_arr.append()
            # board[r][c]
    # print(board, count, q_count);
    if q_count == 0:
        print(answer);
        break;
    answer += 1;
    # print(check);
    
# print(n,l,r);