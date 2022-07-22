import sys;
n, m = map(int, sys.stdin.readline().split());
arr = list(map(int, sys.stdin.readline().split()));

def binary_search(target):
    start = 0;
    end = 999999999;
    max = 0;
    while start <= end:
        mid = (start+end) // 2;
        tmp = 0;
        for i in arr:
            if i - mid <= 0:
                continue;
            else:
                tmp += (i-mid);
        if tmp == target:
            max = mid;
            return max;
        elif tmp > target:
            start = mid + 1;
        elif tmp < target:
            end = mid - 1;
    return max;

print(binary_search(m));