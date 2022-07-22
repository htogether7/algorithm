import sys;
n, m, r = map(int, input().split());

arr = [];

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())));


if n <= m:
    for i in range(r):
        for i in range(int(n/2)):
            tmp = arr[i][i];
            for j in range(i,m-i-1):
                arr[i][j] = arr[i][j+1];

            for j in range(i, n-i-1):
                arr[j][m-i-1] = arr[j+1][m-i-1];

            for j in range(m-1-i,i,-1):
                arr[n-i-1][j] = arr[n-i-1][j-1];

            for j in range(n-1-i,i,-1):
                arr[j][i] = arr[j-1][i];

            arr[i+1][i] = tmp;
else:
    for i in range(r):
        for i in range(int(m/2)):
            tmp = arr[i][m-i-1];
            for j in range(i,n-i-1):
                arr[j][m-i-1] = arr[j+1][m-i-1];
            # print(arr);
            for j in range(m-i-1, i, -1):
                arr[n-i-1][j] = arr[n-i-1][j-1];
            # print(arr);
            for j in range(n-1-i,i,-1):
                arr[j][i] = arr[j-1][i];
            # print(arr);
            for j in range(i,m-i-1):
                arr[i][j] = arr[i][j+1];
            # print(arr);
            arr[i][m-i-2] = tmp;

for i in range(n):
    tmp = "";
    for j in range(m):
        tmp += str(arr[i][j]) + " ";
    print(tmp);