import sys;
input = sys.stdin.readline

n = int(input())
str = input()

l = 0
r = n-1

answer = 0

if str[l] != str[r]:
    tmp_left_index = 0
    tmp_right_index = n-1
    while str[tmp_left_index] == str[l]:
        tmp_left_index += 1
    
    while str[tmp_right_index] == str[r]:
        tmp_right_index -= 1

    if tmp_left_index >= r - tmp_right_index:
        r = tmp_right_index
    else:
        l = tmp_left_index
    answer = 2
else:
    answer = 1
    
while l < r:
    while str[l] == str[l+1]:
        l += 1
    l += 1
    while str[r] == str[r-1]:
        r -= 1
    r -= 1
    if l > r:
        break
    answer += 1

print(answer)

    # print(l,r)
    # print(tmp_left_index, tmp_right_index)
