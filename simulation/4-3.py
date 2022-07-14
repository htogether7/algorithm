n,m = map(int, input().split());
y,x,dir = map(int, input().split());
arr = [];
for i in range(n):
    arr.append(list(map(int,input().split())));
# print(n,m);
# print(y,x,dir);
# print(arr);
dirs = [0, 3, 2, 1];
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]];
count = 1;
arr[y][x] = 2;

while True:
    # if 사방으로 못가고 뒤쪽 방향이 바다면, 멈춘다.

    stop = 1;
    for i in [0,1,3]:
        tmp = dirs[(dirs.index(dir) + i) % 4];
        dy,dx = directions[tmp];
        if arr[y+dy][x+dx] == 0:
            stop = 0;
            break;
    if stop == 1:
        tmp = dirs[(dirs.index(dir) + 2) % 4];
        dy, dx = directions[tmp];
        if arr[y+dy][x+dx] == 1:
            pass;
        elif arr[y+dy][x+dx] == 2:
            y = y+dy;
            x = x+dx;
            stop = 0;
        elif arr[y+dy][x+dx] == 0:
            stop = 0;
    if stop == 1:
        break;

    dir = dirs[(dirs.index(dir) + 1) % 4];
    dy, dx = directions[dir];
    if arr[y+dy][x+dx] == 0:
        arr[y+dy][x+dx] = 2;
        y = y + dy;
        x = x + dx;
        count += 1;
    # print(y,x);
    # print(dir);
    # print(arr);
    # roofCount += 1;
print(count);