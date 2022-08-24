import sys;
import math;
input = sys.stdin.readline;

n,m = map(int, input().split());

board = [list(map(int, list(input().rstrip()))) for _ in range(n)];

dys = [i for i in range(-n,n)];
dxs = [i for i in range(-m,m)];
max_result = -1;

for y in range(n):
    for x in range(m):
        for dy in dys:
            for dx in dxs:
                if dy == 0 and dx == 0:
                    continue;
                # print(y,x,dy,d    x)
                now_y = y;
                now_x = x;
                tmp = [];
                while 0<= now_y < n and 0 <= now_x < m:
                    tmp.append(str(board[now_y][now_x]));
                    now_y += dy;
                    now_x += dx;
                    if int(math.sqrt(int("".join(tmp)))) == math.sqrt(int("".join(tmp))):
                        max_result = max(max_result, int("".join(tmp)));
                # print(tmp);
print(max_result);