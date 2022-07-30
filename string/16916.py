from collections import deque;
s = input();
p = input();

# l = 0;
# if len(s) < len(p):
#     print(0);
# else:
#     r = len(p);
#     tmp = deque([]);
#     for i in range(len(p)):
#         tmp.append(s[i]);
#     contains = False;
#     while r <= len(s):
#         if tmp[0] == p[0] and tmp[-1] == p[-1]:
#             if "".join(tmp) == p:
#                 contains = True;
#                 break;
#         if r < len(s):
#             tmp.popleft();
#             tmp.append(s[r]);
#         # print(tmp);
#         r += 1;
#     if contains == True:
#         print(1);
#     else:
#         print(0);
if p in s:
    print(1);
else:
    print(0);