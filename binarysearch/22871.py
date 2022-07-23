# import sys
# input = sys.stdin.readline;
# n = int(input());
# # s = 1;
# e = int(1e9);

# arr = list(map(int, sys.stdin.readline().split()));
# dp = [e] * n;
# dp[0] = 0;

# for i in range(0, len(arr)-1):
#     for j in range(i+1, len(arr)):
#         tmp = max((j-i) * (1 + abs(arr[i]-arr[j])), dp[i])
#         dp[j] = min(dp[j], tmp);
# print(dp[-1]);


import sys;

input = sys.stdin.readline;
INF = 999999999
n = int(input())
A = list(map(int, input().split()))
dp = [0] + [INF] * (n - 1)

for i in range(1, n):
    for j in range(0, i):
         power = max((i - j) * (1 + abs(A[i] - A[j])), dp[j]);
         dp[i] = min(dp[i], power)

print(dp[-1])
# mid = 0;
# def step(num):
#     start = 0;
#     end = 1;
#     while end <= len(arr)-1:
#         # while num >= (end-start) * (1 + abs(arr[start] - arr[end])):
#         #     end += 1;
#         #     if end > len(arr) - 1:
#         #         return True;
#         # end -= 1;
#         # if start == end and:
#         #     return False;
#         # else:
#         #     start = end;
#         #     end += 1;
#         tmp = 0;
#         for e in range(end, len(arr)):
#             if num >= (e-start) * (1 + abs(arr[start] - arr[e])):
#                 tmp = e;
#         # print(tmp);

#         if tmp == 0:
#             return False;
#         elif tmp == len(arr)-1:
#             return True;
#             # break;
#         else:
#             start = tmp;
#             end = start + 1;
# target = 0;

# if len(set(arr)) == 1:
#     print(1);
# else:
#     while s < e:
#         # print("hi1");
#         # if s == e:
#         #     # print(s);
#         #     break;
#         # else:
#         mid = (s+e) // 2;
#         print(s,e, mid, target)
#         # print(mid, step(mid));
#         if step(mid):
#             # print(mid);
#             e = mid - 1;
#             target = mid;
#             # print(target);
#         else:
#             s = mid + 1;
#     if step(s):
#         print(s);
#     print(target);