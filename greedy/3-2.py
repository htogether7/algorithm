n, m, k = map(int, input().split());
arr = list(map(int, input().split()));

arr.sort(reverse=True);

second_count = m // (k+1);
first_count = m - second_count;

print(first_count * arr[0] + second_count * arr[1]);