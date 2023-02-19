import sys
n = int(input())
# result = [{} for _ in range(15)]
result = []
# print(result)
for _ in range(n):
    info = input().split()
    result.append(info[1:])
    # for index in range(1, len(info)):
    #     # if index == 1:
    #     #     if index == 2:
    #     #         result[0][info[index]] = []
    #     #     else:
    #     #         result[0][info[index]] = 
    #     # else:
    #     if index == len(info) - 1:
    #         if info[index] in result[index-1]:
    #             continue
    #         result[index-1][info[index]] = []
    #     else:
    #         if info[index] in result[index-1]:
    #             result[index-1][info[index]].append(info[index+1])
    #             continue
    #         result[index-1][info[index]] = [info[index+1]]
result.sort()
# answer = []
# def dfs(l,s):
#     # key_list = []
#     next_arr = result[l][s]
#     # key_list.sort()
#     if not next_arr:
#         return
#     # print(key_list)
#     for str in next_arr:
#         answer.append((l+1,str))
#         # print(l+1,str, key_list)
#         dfs(l+1, str)
#         # answer.pop()
# arr = list(result[0].keys())
# arr.sort()
# for key in arr:
#     answer.append((0,key))
#     dfs(0,key)

# for (l,s) in answer:
#     print('--' * l + s)
# print(answer)
# check_dict = [set() for _ in range(15)]
# for s in result:
#     for i,c in enumerate(s):
#         if i == 0:
#             if (c,0) in check_dict[i]:
#                 continue
#             check_dict[i].add((c,0))

        # if c in check_dict[i]:
        #     continue
        # else:
        #     print('--' * i + c)
        #     check_dict[i].add(c)
start = 0
for result_index,r in enumerate(result):
    for i in range(start,len(r)):
        print("--" * i + r[i])
    
    if result_index == len(result)-1:
        continue

    for compare_index in range(min(len(result[result_index]), len(result[result_index+1]))):
        if result[result_index][compare_index] != result[result_index+1][compare_index]:
            start = compare_index
            break
# print(result)