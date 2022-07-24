import sys;
input = sys.stdin.readline;
n = int(input());

arr = list(map(int, input().split()));
arr.sort();

l = 0;
r = len(arr) - 1;
min = arr[l] + arr[r];
left = l;
right = r;

if arr[0] < 0 and arr[-1] < 0:
    print(f"{arr[-2]} {arr[-1]}");
    # print(arr[-2], arr[-1]);
elif arr[0] > 0 and arr[-1] > 0:
    print(f"{arr[0]} {arr[1]}");
    # print(arr[0], arr[1]);
else:

    
    while l < r:
        if abs(min) > abs(arr[l] + arr[r]):
            min = arr[l] + arr[r];
            left = l;
            right = r;
        if abs(arr[l+1] + arr[r]) > abs(arr[l] + arr[r-1]):
            r -= 1;
        else:
            l += 1;

        
    print(f"{arr[left]} {arr[right]}");
# print(arr);