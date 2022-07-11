n = int(input());
arr = list(map(int,input().split()));
l = 0;
r = 1;
count = 0;
while l != len(arr)-1 or r != len(arr)-1:
    if sum(arr[l:r+1]) == 0:
        count+=1;
        l += 1;
    else:
        if l == r:
            r += 1;
        elif r == len(arr) - 1:
            l += 1;
        else:
            if abs(sum(arr[l+1:r+1])) <= abs(sum(arr[l:r+2])):
                l += 1;
            else:
                r += 1;
print(count);