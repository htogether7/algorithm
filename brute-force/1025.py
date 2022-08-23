import sys;
import math;
input = sys.stdin.readline;

n,m = map(int, input().split());

board = [list(map(int, list(input().rstrip()))) for _ in range(n)];

dy = [i for i in range(-n+1,n)];
dx = [i for i in range(m)];
max_result = -1;
# print(dy);
for i in dy:
    for j in range(len(dx)):
        # print(i,j);
        if i == 0 and j == 0:
            for y in range(n):
                for x in range(m):
                    if int(math.sqrt(board[y][x])) == math.sqrt(board[y][x]):
                        max_result = max(max_result, board[y][x]);
        else:
            if i >= 0:
                for y in range(0,n-i):
                    for x in range(0,m-j):
                        # print(y,x,i,j);
                        tmp = [];
                        # tmp.append((y,x));
                        now_y = y;
                        now_x = x;
                        while now_y < n and now_x < m:
                            tmp.append((now_y,now_x));
                            now_y += i;
                            now_x += j;
                        # print(i,j);
                        # print(tmp);
                        string_tmp = [];
                        for pos in tmp:
                            string_tmp.append(board[pos[0]][pos[1]]);
                        if len(string_tmp) != 0:
                            # print(string_tmp, i, j);
                            # result = ("".join(string_tmp))
                            result = 0;
                            for l in range(len(string_tmp)):
                                result += string_tmp[l] * (10 ** (len(string_tmp)-1-l));
                            # print(string_tmp);
                            # print(result**(1/2));
                            if int(math.sqrt(result)) == math.sqrt(result):
                                max_result = max(max_result, result);
                                # print(result);
                            string_tmp.reverse();
                            result = 0;
                            for l in range(len(string_tmp)):
                                result += string_tmp[l] * (10 ** (len(string_tmp)-1-l));
                            if int(math.sqrt(result)) == math.sqrt(result):
                                max_result = max(max_result, result);
                            # print(result);
            else:
                # print(i,j);
                for y in range(n-1, -i-1, -1):
                    for x in range(0,m-j):
                        # print(y,x);
                        tmp = [];
                        # tmp.append((y,x));
                        now_y = y;
                        now_x = x;
                        while 0 <= now_y < n and now_x < m:
                            tmp.append((now_y,now_x));
                            now_y += i;
                            now_x += j;
                        # print(i,j);
                        # print(tmp);
                        string_tmp = [];
                        for pos in tmp:
                            string_tmp.append(board[pos[0]][pos[1]]);
                        if len(string_tmp) != 0:
                            # print(string_tmp, i, j);
                            # result = ("".join(string_tmp))
                            result = 0;
                            for l in range(len(string_tmp)):
                                result += string_tmp[l] * (10 ** (len(string_tmp)-1-l));
                            # print(string_tmp);
                            # print(result**(1/2));
                            if int(math.sqrt(result)) == math.sqrt(result):
                                max_result = max(max_result, result);
                                # print(result);
                            string_tmp.reverse();
                            result = 0;
                            for l in range(len(string_tmp)):
                                result += string_tmp[l] * (10 ** (len(string_tmp)-1-l));
                            if int(math.sqrt(result)) == math.sqrt(result):
                                max_result = max(max_result, result);

                    # print(string_tmp);
                    # print(result**(1/2));

                    # print("".join)
# if max_result == 0:
#     print(-1);
# else:
print(max_result);

# for j in range(1, len(dx)):


# print(board);