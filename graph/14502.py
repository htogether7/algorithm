import sys;
from collections import deque
import copy;


input = sys.stdin.readline;

n, m = map(int, input().rstrip().split());

board = [list(map(int, input().rstrip().split()))for _ in range(n)];

# board_copy = [board[i][::] for i in range(n)];

zeros = [];
max_safe_zone = 0;
for y in range(n):
    for x in range(m):
        if board[y][x] == 0:
            zeros.append((y,x));

# print(zeros);

dx = [1,-1,0,0,];
dy = [0,0,1,-1];

count = 0;

def dfs(count):
    global max_safe_zone;
    if count == 3:
        tmp_count = 0;
        # tmp_board = [board[i][::] for i in range(n)];
        tmp_board = copy.deepcopy(board);
        check_break = False;
        for y in range(n):
            for x in range(m):
                if tmp_board[y][x] == 2:
                    q = deque([(y,x)]);
                    while len(q) != 0:
                        next = q.popleft();
                    #     # print(q);
                        for ind in range(4):
                            if 0 <= next[0] + dy[ind] < n and 0 <= next[1] + dx[ind] < m and tmp_board[next[0]+dy[ind]][next[1]+dx[ind]] == 0:
                                q.append((next[0] + dy[ind], next[1] + dx[ind]));
                                tmp_board[next[0] + dy[ind]][next[1] + dx[ind]] = 2;
                                tmp_count += 1;
        max_safe_zone = max(max_safe_zone, len(zeros) - 3 - tmp_count)
        return;

    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                board[y][x] = 1;
                dfs(count+1);
                board[y][x] = 0;

dfs(0);

# for i in range(len(zeros)-2):
#     for j in range(1, len(zeros)-1):
#         for k in range(2, len(zeros)):
#             board[zeros[i][0]][zeros[i][1]] = 1;
#             board[zeros[j][0]][zeros[j][1]] = 1;
#             board[zeros[k][0]][zeros[k][1]] = 1;
#             # print(board);
#             tmp_count = 0;
#             check_break = False;
#             for y in range(n):
#                 for x in range(m):
#                     if board[y][x] == 2:
#                         q = deque([(y,x)]);
#                         while len(q) != 0:
#                             next = q.popleft();
#                         #     # print(q);
#                             for ind in range(4):
#                                 if 0 <= next[0] + dy[ind] < n and 0 <= next[1] + dx[ind] < m and board[next[0]+dy[ind]][next[1]+dx[ind]] == 0:
#                                     q.append((next[0] + dy[ind], next[1] + dx[ind]));
#                                     board[next[0] + dy[ind]][next[1] + dx[ind]] = 2;
#                                     tmp_count += 1;
#                                     if tmp_count == len(zeros) - 3:
#                                         check_break = True;
#                                         break;
#                             if check_break:
#                                 break;
#                     if check_break:
#                         break;
#                 if check_break:
#                     break;
#                         # print("finish");
#             # for y in range(n):
#             #     for x in range(m):
#             #         if board[y][x] == 0:
#             #             tmp_count += 1;
#             # max_safe_zone = max(tmp_count, max_safe_zone)
#             # print(max_safe_zone)
#             max_safe_zone = max(max_safe_zone, len(zeros) - 3 - tmp_count)
#             board = [board_copy[s][::] for s in range(n)];

print(max_safe_zone);