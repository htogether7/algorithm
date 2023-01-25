import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

def check_possible(n):
    board = [input().rstrip() for _ in range(n)]
    board.sort(key = lambda x : -len(x))

    dict_arr = [defaultdict(set) for _ in range(10)]
    # print(dict_arr)

    for num in board:
        check_include = True
        if len(num) == 0:
            return False
        # print("num",num)
        for ind, s in enumerate(num):
            if int(s) not in dict_arr[ind]:
                check_include = False
            # if len(dict_arr[ind][int(s)]) == 1 and -1 in dict_arr[ind][int(s)]:
                # check_include = False
            if ind == len(num)-1:
                dict_arr[ind][int(s)].add(-1)
            else:
                # if -1 in dict_arr[ind][int(s)]:
            #         print(dict_arr)
            #         return False
                dict_arr[ind][int(s)].add(int(num[ind+1]))
        # print(num, check_include)
        if check_include:
            return True
        # print(dict_arr)
    return False

result = []
for _ in range(t):
    n = int(input())
    if check_possible(n):
        result.append("NO")
        # result.append("YES")
    else:
        result.append("YES")
        # result.append("NO")

# print(result)
for r in result:
    print(r)

    # print(dict_arr)
    # for num in board:
        # for ind,s in enumerate(num):
            # board[ind][int(s)]
    # print(dict_arr)
    # print(path)
    # print(board)
    # print(board)