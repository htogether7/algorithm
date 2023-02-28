# import sys
# input = sys.stdin.readline

# n = int(input())

# weights = [*map(int,input().split())]
# weights.sort()
# weight_set = set([0])

# def check(max_weight, tmp_set):
#     num = max_weight + 1
#     count = 0
#     while True:
#         if num in tmp_set:
#             num += 1
#             count += 1
#         else:
#             if count == len(tmp_set):
#                 return 0
#             else:
#                 return num

#     # num = 1
#     # while True:
#     #     if num in weight_set:
#     #         num += 1
#     #     else:
#     #         return num



# def find_min(weights, weight_set):
#     max_weight = 0
#     for weight in weights:
#         tmp_set = set()
#         for plus in weight_set:
#             if weight + plus not in weight_set:
#                 # if weight+plus-1 not in weight_set and weight+plus+1 not in tmp_set:
                    
#                 tmp_set.add(weight + plus)

#             max_weight = plus
#             print(plus, weight, weight_set, tmp_set)
#         # print(tmp_set)
#         # print(weight_set)
        
#         check_result = check(max_weight, tmp_set)
#         # max_weight = 
#         if check_result == 0:
#             weight_set = weight_set.union(tmp_set)
#         else:
#             return check_result
# print(find_min(weights, weight_set))
# # print(weight_set)
# # print(weight_set)

# # print(weights)


import sys
input = sys.stdin.readline

n = int(input())

weights = [*map(int,input().split())]
weights.sort()

sum = 0
check_finish = False
for weight in weights:
    if weight > sum + 1:
        print(sum+1)
        check_finish = True
        break
    else:
        sum += weight

if not check_finish:
    print(sum+1)
    # print(sum)
    # if weight <= sum:
    #     continue
    # else:
    #     if sum+1 != weight:
    #         print(sum+1)
    #         break
    #     else:
    #         sum += weight
    #         print(sum)



# weight_set = set([0])

# def check(weight_set,start):
#     num = start
#     while True:
#         if num in weight_set:
#             num += 1
#         else:
#             return num



# def find_min(weights, weight_set):
#     max_weight = 0
#     for plus in weight_set:
#         tmp_set = set()
#         for weight in weights:
#             max_weight = max(max_weight, weight+plus)
#             weight
#             tmp_set.add(weight + plus)
#         print(weight_set, tmp_set)
#         # weight_set = weight_set.union(tmp_set)
#     return check(weight_set, start)

# print(find_min(weights, weight_set))