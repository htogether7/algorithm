import sys;
input = sys.stdin.readline;

n,m = map(int, input().split());

ground = list(map(int, input().split()));


commands = [];

for _ in range(m):
    commands.append(list(map(int, input().split())));

# print(commands);

for command in commands:
    s,e,h = command;
    for i in range(s-1, e):
        ground[i] += h;
    # print(s-1,e-1,h);
print(*ground);