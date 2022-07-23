import sys;
input = sys.stdin.readline;
t = int(input());

for _ in range(t):
    mn = int(1e9);
    mx = -1;

    four_dict = {};

    str = input().strip();
    k = int(input());

    for ind, s in enumerate(str):
        if s in four_dict:
            four_dict[s].append(ind);
        else:
            four_dict[s] = [ind];
    
    for arr in four_dict.values():
        if len(arr) >= 2:
            for ind in range(len(arr)-(k-1)):
                mx = max(mx, arr[ind+k-1]-arr[ind] + 1);
                mn = min(mn, arr[ind+k-1] - arr[ind] + 1);
    if mx == -1:
        print(-1);
    else:
        print(f"{mn} {mx}");



