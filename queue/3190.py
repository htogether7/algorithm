import sys;
from collections import deque;

n = int(input());
pos = deque();
pos.append([0,0]);

pos2 = deque();
pos2.append("0,0");

num_apples = int(input());
apples = {};


for i in range(num_apples):
    r,c = sys.stdin.readline().split();
    # apples.append([int(r),int(c)]);
    if int(r)-1 in apples:
        apples[int(r)-1].append(int(c)-1);
    else:
        apples[int(r)-1] = [int(c)-1];

num_change = int(input());
change = {}

for i in range(num_change):
    t, d = sys.stdin.readline().split();
    change[int(t)] = d;


# print(apples);
# print(change);

time = 0;
directions = {
    "r" : [0,1],
    "l" : [0,-1],
    "u" : [-1,0],
    "d" : [1,0]
}
dir = "r";
while pos and pos[-1][0] >= 0 and pos[-1][0] <= n-1 and pos[-1][1] >= 0 and pos[-1][1] <= n-1:
    if time in change:
        if change[time] == "D":
            if dir == "r":
                dir = "d";
            elif dir == "d":
                dir = "l";
            elif dir == "l":
                dir = "u";
            elif dir == "u":
                dir = "r";
        elif change[time] == "L":
            if dir == "r":
                dir = "u";
            elif dir == "u":
                dir = "l";
            elif dir == "l":
                dir = "d";
            elif dir == "d":
                dir = "r";
    # next = directions[dir] + pos[-1];
    next = [directions[dir][0] + pos[-1][0], directions[dir][1] + pos[-1][1]];
    str_next = [str(next[0]), str(next[1])];
    pos.append(next);
    pos2.append(",".join(str_next));

    if len(pos2) != len(set(pos2)):
        time += 1;
        break;

    if next[0] not in apples:
        pos.popleft();
        pos2.popleft();
    else:
        if next[1] not in apples[next[0]]:
            pos.popleft();
            pos2.popleft();   
        else:
            apples[next[0]].remove(next[1]); 
    time += 1;
    # print(pos);
print(time);

