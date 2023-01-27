import sys
n = int(input())

num_list = []

answer = 10 ** (n)

def check_bad(s):
    global num_list
    copy_num_list = num_list[::]
    if s:

        copy_num_list.append(s)

    if len(copy_num_list) == 1:
        return False
    
    for i in range(1, (len(copy_num_list) // 2) + 1):
        right_arr = copy_num_list[len(copy_num_list) - i:] 
        left_arr =  copy_num_list[len(copy_num_list) - i * 2 :len(copy_num_list) - i]
        right_str = "".join(right_arr)
        left_str = "".join(left_arr)

        if right_str == left_str:
            return True
    return False


# def dfs(l):
#     global answer
#     if l == n:
#         # answer = min(answer, int("".join(num_list)))
#         print("".join(num_list))
#         # print(num_list)
#         # print(l)
#         return 
#     # print(num_list)
#     for i in range(1,4):
#         # print(num_list)
#         if check_bad(str(i)):
#             continue

#         num_list.append(str(i))
#         dfs(l+1)
#         num_list.pop()

while len(num_list) < n:
    print(num_list)
    # if check_bad(''):
        # num_list.pop()
        # continue
    check_impossible = True
    for i in range(1,4):
        if check_bad(str(i)):
            continue
        else:
            num_list.append(str(i))
            check_impossible = False
            break

    if check_impossible:
        last = int(num_list.pop())
        # check_insert = False
        for j in range(last+1,4):
            if check_bad(str(j)):
                continue
            else:
                num_list.append(str(i))
                # check_insert = True
                break

        # if not check_insert:
    while check_bad(''):
        last = num_list.pop()
        if last == 3:
            while True:
                last2 = num_list.pop()
                if last2 != 3:
                    check_insert = False
                    for i in range(int(last2)+1, 4):
                        if check_bad(str(i)):
                            continue
                        num_list.append(str(i))
                        check_insert = True
                        break
                if check_insert:
                    break
                # else:


        else:

print("".join(num_list))        
# print(answer)

# for i in range(n):
    # for 