import sys;
from collections import deque
from xml.etree.ElementTree import TreeBuilder;
input = sys.stdin.readline;
w, h = map(int, input().split());

board = [list(map(int, input().split())) for _ in range(h)];

# print(board);

checked = [[0]*w for _ in range(h)];

result = 0;

even_dy = [-1,-1,0,0,1,1]
even_dx = [-1,0,-1,1,-1,0];

odd_dy = [-1,-1,0,0,1,1];
odd_dx = [0,1,-1,1,0,1];

for i in range(h):
    for j in range(w):
        if board[i][j] == 1 and checked[i][j] == 0:
            q = deque([[i,j]]);
            checked[i][j] = 1;
            while q:
                next = q.popleft();
                
                if next[0] % 2 == 1:
                    tmp_count = 0;
                    for k in range(6):
                        dy = even_dy[k];
                        dx = even_dx[k];
                        if 0 <= next[0]+dy < h and 0 <= next[1]+dx < w:
                            if board[next[0]+dy][next[1]+dx] == 1:
                                tmp_count += 1;
                                if checked[next[0]+dy][next[1]+dx] == 0:
                                    q.append([next[0]+dy, next[1]+dx]);
                                    checked[next[0]+dy][next[1]+dx] = 1;
                        # else:
                        #     tmp_count += 1;
                    result += (6-tmp_count);

                else:
                    tmp_count = 0;
                    for k in range(6):
                        dy = odd_dy[k];
                        dx = odd_dx[k];
                        if 0 <= next[0]+dy < h and 0 <= next[1]+dx < w:
                            if board[next[0]+dy][next[1]+dx] == 1:
                                # print(next[0]+dy, next[1]+dx);
                                tmp_count += 1;
                                if checked[next[0]+dy][next[1]+dx] == 0:
                                    q.append([next[0]+dy, next[1]+dx]);
                                    checked[next[0]+dy][next[1]+dx] = 1;
                        # else:
                        #     tmp_count += 1;
                    result += (6-tmp_count);


around_checked = [[0]*w for _ in range(h)];

for i in range(h):
    for j in range(w):
        if board[i][j] == 0 and around_checked[i][j] == 0:
            q = deque([[i,j]]);
            around_checked[i][j] = 1;
            tmp = 0;
            break_check = False;
            while q:
                if break_check:
                    break;
                next = q.popleft();
                if next[0] % 2 == 1:
                    tmp_count = 0;
                    for k in range(6):
                        dy = even_dy[k];
                        dx = even_dx[k];
                        if 0 <= next[0]+dy < h and 0 <= next[1]+dx < w:
                            if board[next[0]+dy][next[1]+dx] == 0:
                                tmp_count += 1;
                                # print(next);
                                if around_checked[next[0]+dy][next[1]+dx] == 0:
                                    q.append([next[0]+dy, next[1]+dx]);
                                    around_checked[next[0]+dy][next[1]+dx] = 1;
                        else:
                            break_check = True;
                            break;
                    tmp += (6-tmp_count);
                    # print(next, tmp);
                else:
                    tmp_count = 0;
                    for k in range(6):
                        dy = odd_dy[k];
                        dx = odd_dx[k];
                        if 0 <= next[0]+dy < h and 0 <= next[1]+dx < w:
                            if board[next[0]+dy][next[1]+dx] == 0:
                                tmp_count += 1;
                                # print(next)
                                if around_checked[next[0]+dy][next[1]+dx] == 0:
                                    q.append([next[0]+dy, next[1]+dx]);
                                    around_checked[next[0]+dy][next[1]+dx] = 1;
                        else:
                            break_check = True;
                            break;
                    tmp += (6-tmp_count);
                    # print(next, tmp);
            if break_check == False:
                result -= tmp;
                # print(result);
            # print(next, result);



print(result);