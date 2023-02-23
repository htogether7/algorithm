import sys
input = sys.stdin.readline
p = list(input().rstrip())

def cal_ppap(p):
    p_count = 0
    # for i,char in enumerate(p):
    index = 0
    while index < len(p):
        if p[index] == "P":
            p_count += 1
            index += 1
        else:
            if p_count < 2:
                return False
            if index == len(p)- 1 or p[index+1] == "A":
                return False
            p_count -= 1
            index += 2
        # print(index,p_count)
    if p_count <= 1:
        return True
    # print(p_count)

# cal_ppap(p)
# print(p)
if "".join(p) == "P":
    print("PPAP")
else:
    # if "A" not in p:
    #     print("NP")
    # else:
    if cal_ppap(p):
        print("PPAP")
    else:
        print("NP")

