import sys
input = sys.stdin.readline

x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

l1_start = min(x1,x2)
l1_end = max(x1,x2)

l2_start = min(x3,x4)
l2_end = max(x3,x4)

range_start = min(l1_start, l2_start)
range_end = max(l1_end, l2_end)

check_vertical_l1 = False
check_vertical_l2 = False

if x1 == x2:
    check_vertical_l1 = True

if x3 == x4:
    check_vertical_l2 = True

def y_l1(x):
    return ((y1-y2) / (x1-x2)) * (x - x1) + y1

def y_l2(x):
    return ((y3-y4) / (x3-x4)) * (x - x3) + y3

def check():
    if check_vertical_l1 and check_vertical_l2:
        if x1 != x3:
            return False
        else:
            return True
        
    elif check_vertical_l1:
        if l2_start <= x1 <= l2_end:
            if min(y1,y2) <=y_l2(x1) <= max(y1,y2):
                return True
            else:
                return False
        else:
            return False

    elif check_vertical_l2:
        if l1_start <= x3 <= l1_end:
            if min(y3,y4) <= y_l1(x3) <= max(y3,y4):
                return True
            else:
                return False
        else:
            return False

    else:

        for x in range(range_start, range_end+1):
            l1_check = False
            l2_check = False
            
            if l1_start <= x <= l1_end:
                l1_check = True

            if l2_start <= x <= l2_end:
                l2_check = True

            if l1_check == False or l2_check == False:
                continue

            now_l1_y = y_l1(x)
            now_l2_y = y_l2(x)

            if now_l1_y == now_l2_y:
                return True
            elif now_l1_y > now_l2_y:
                for j in range(x+1, min(l1_end,l2_end)+1):
                    if y_l1(j) <= y_l2(j):
                        return True
            else:
                for j in range(x+1, min(l1_end, l2_end)+1):
                    if y_l1(j) >= y_l2(j):
                        return True

        return False
# print(check_range())

print(int(check()))