import sys;

input = sys.stdin.readline;

n,s = map(int, input().split());

arr = list(map(int, input().split()));

# if 

l = 0;
r = 0;
sum = arr[l];
min_length = int(1e6);

while l <= r:
    if r == n-1:
        if sum < s:
            break;
        else:
            min_length = min(min_length, r-l+1);
            sum -= arr[l];
            l += 1;
            # print(l,r );
            # print(min_leng/th);

    else:
        if sum < s:
            r += 1;
            sum += arr[r];
            # print(l,r );
            # print(min_length);

        elif sum >= s:
            min_length = min(min_length, r-l+1);
            sum -= arr[l];
            l += 1;
            # print(l,r );
            # print(min_leng/th);
    
if min_length == int(1e6):
    print(0);
else:
    print(min_length);
    