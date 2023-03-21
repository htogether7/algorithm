import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def d(num):
    if num < 5000:
        return 2*num;
    else:
        return (2*num) % 10000

def s(num):
    if num == 0:
        return 9999
    else:
        return num-1
    
def l(num):
    num_to_string_list = list(str(num))
    if len(num_to_string_list) == 4:
        result_list = num_to_string_list[1:] + [num_to_string_list[0]]
        return int("".join(result_list))
    else:
        zero_list = ["0"] * (4-len(num_to_string_list))
        new_list = zero_list + num_to_string_list
        result_list = new_list[1:] + [new_list[0]]
        return int("".join(result_list))

def r(num):
    num_to_string_list = list(str(num))
    if len(num_to_string_list) == 4:
        result_list = [num_to_string_list[-1]] + num_to_string_list[:-1]
        return int("".join(result_list))
    else:
        zero_list = ["0"] * (4-len(num_to_string_list))
        new_list = zero_list + num_to_string_list
        result_list = [new_list[-1]] + new_list[:-1]
        return int("".join(result_list))

def find_shortest_path(a,b):
    check = [""] * 10000
    q = deque()
    q.append(a)
    while q:
        num = q.popleft()
        after_d = d(num)
        after_s = s(num)
        after_l = l(num)
        after_r = r(num)

        check_value = ""
        if num != a:
            check_value = check[num]

        if check[after_d] == "":
            check[after_d] = check_value +"D"
            q.append(after_d)
        if check[after_s] == "":
            check[after_s] = check_value +"S"
            q.append(after_s)
        if check[after_l] == "":
            check[after_l] = check_value + "L"
            q.append(after_l)
        if check[after_r] == "":
            check[after_r] = check_value + "R"
            q.append(after_r)
        if check[b] != "":
            return check[b]

result = []
for _ in range(t):
    a,b = map(int, input().split())
    result.append(find_shortest_path(a,b))

for r in result:
    print(r)
    


