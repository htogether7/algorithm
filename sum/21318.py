import sys;
input = sys.stdin.readline;

n = int(input());
arr = list(map(int, input().split()));

q = int(input());

tmp = [];
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        tmp.append(1);
    else:
        tmp.append(0);
tmp.append(0);

sum = [0];
count = 0;
for i in tmp:
    if count == 0:
        if i == 1:
            count += 1;
        sum.append(sum[-1]);
    else:
        sum.append(count + sum[-1]);
        if i == 0:
            count = 0;
    # if i == 1:
    #     count += 1;
    #     sum.append(sum[-1]);
    


for _ in range(q):
    x,y = map(int, input().split());
    x -= 1;
    y -= 1;
    if x == y:
        print(0);
    else:
        if tmp[x-1] == 1:
            print(sum[y+1]-sum[x]-1);
        else:
            print(sum[y+1]-sum[x]);
# print(tmp);
# print(sum);


# print(tmp);

# for _ in range(q):
