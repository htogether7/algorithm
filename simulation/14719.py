import enum
import sys;
input = sys.stdin.readline;

h, w = map(int, input().split());

board = list(map(int, input().split()));

result = 0;
blocks = [[] for _ in range(h+1)];
for ind, x in enumerate(board):
    # result -= x;
    for i in range(1,x+1):
        blocks[i].append(ind);
    # blocks[x].append(ind);

# print(result);
for i in range(1, len(blocks)):
    if len(blocks[i]) >1:
        for j in range(len(blocks[i])-1):
            result += blocks[i][j+1] - blocks[i][j]-1;

print(result);