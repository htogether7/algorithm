# import sys
# from collections import defaultdict
# n = int(input())
# arr = []
# answer = 0
# ab = []
# cd = []
# for _ in range(n):
#     arr.append(list(map(int,sys.stdin.readline().split())))

# # print(arr)    

# # dict_1 = defaultdict(int)
# # dict_2 = defaultdict(int)
# ab = []
# cd = []
# dict_ab = defaultdict(int)
# # dict_cd = defaultdict(int)
# for i in range(n):
#     for j in range(n):
#         dict_ab[arr[i][0] + arr[j][1]] += 1
#         # dict_cd[arr[i][2] + arr[j][3]] += 1
#         # ab.append(arr[i][0] + arr[j][1])
#         # cd.append(arr[i][2] + arr[j][3])
# ab_keys = list(dict_ab.keys())
# # cd_keys = list(dict_cd.keys())
# ab_keys.sort()
# # cd_keys.sort()
# # ab.sort()
# # cd.sort()

# p1 = 0
# p2 = len(cd_keys)-1
# count = 0
# while p1 < len(ab_keys) and p2 >= 0:
#     if count == 2:
#         break
#     if ab_keys[p1] + cd_keys[p2] == 0:
#         answer += dict_ab[ab_keys[p1]] * dict_cd[cd_keys[p2]]
#         if abs(ab_keys[p1] - ab_keys[p1+1]) >= abs(cd_keys[p2] - cd_keys[p2-1]):
#             p2 -= 1
#         else:
#             p1 += 1
#     elif ab_keys[p1] + cd_keys[p2] > 0:
#         p2 -= 1
#     else:
#         p1 += 1
# #     # count += 1
# #     print(p1,p2)
# # print(ab)
# # print(cd)
# print(answer)
# print(dict_1)
# print(dict_2)



import sys
input = sys.stdin.readline
# from collections import defaultdict

N = int(input())
arrA, arrB, arrC, arrD = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    arrA.append(a)
    arrB.append(b)
    arrC.append(c)
    arrD.append(d)

dict_AB = {}
ans = 0

for i in range(N):
    for j in range(N):
        if arrA[i] + arrB[j] not in dict_AB:
            dict_AB[arrA[i] + arrB[j]] = 1
        else:
            dict_AB[arrA[i] + arrB[j]] += 1

for i in range(N):
    for j in range(N):
        cur = arrC[i] + arrD[j]
        cur *= -1
        if cur in dict_AB:
            ans += dict_AB[cur]

print(ans)