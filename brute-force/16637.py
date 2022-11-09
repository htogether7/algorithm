import sys
input = sys.stdin.readline

n = int(input())
str = input().rstrip()
num = n // 2
answer = -999999999999999
count = 0
check = [0] * num

def make_max(arr):
    strList = list(str)
    # length = len(arr);
    # print(strList)
    tmp_arr = [int(strList[0])]

    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] == 1:
            tmp = 0
            if strList[2*i+1] == "+":
                tmp = tmp_arr[-1] + int(strList[2*i+2])

            elif strList[2*i+1] == "*":
                tmp = tmp_arr[-1] * int(strList[2*i+2])
            
            elif strList[2*i+1] == "-":
                tmp = tmp_arr[-1] - int(strList[2*i+2])
            # strList.insert(2*i+3, tmp)
            # del strList[2*i:2*i+3]
            # length -= 1
            # print(tmp)
            # print(strList[2*i], strList[2*i+1], strList[2*i+2])
            tmp_arr[-1] = tmp
            # if arr == [0,0,1,0,1,0,1,0,1]:
                # print(tmp_arr)
        else:
            tmp_arr.append(strList[2*i+1])
            tmp_arr.append(int(strList[2*i+2]))
    
    tmp_max = int(tmp_arr[0])
    # print(strList)
    for i in range(1, len(tmp_arr)):
        if tmp_arr[i] == "+":
            tmp_max += int(tmp_arr[i+1])
            i+=2
        
        elif tmp_arr[i] == "-":
            tmp_max -= int(tmp_arr[i+1])
            i+=2
        elif tmp_arr[i] == "*":
            tmp_max *= int(tmp_arr[i+1])
            i+=2
    # print(tmp_max)
    # if arr == [0,0,1,0,1,0,1,0,1]:
        # print(tmp_max)
    # print(list(str))
    # answer = max(answer, tmp_max)
    # print(answer)
    return tmp_max

def check_possible(arr):
    possible = True
    for i in range(len(arr) - 1):
        if arr[i] == 1 and arr[i+1] == 1:
            possible = False
            break
    return possible


def dfs(l,n):
    global answer
    if l == num-1:
        check[l] = n
        # print(check_possible(check), check)
        if check_possible(check):
            answer = max(answer,make_max(check))
        return
    check[l] = n
    for i in [0,1]:
        dfs(l+1,i)

if n != 1:
    for i in [0,1]:
        dfs(0,i)
    print(answer)
else:
    print(int(str))



