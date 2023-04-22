import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    s_m,s_d,e_m,e_d = map(int,input().split())
    arr.append((s_m,s_d,e_m,e_d))



arr.sort(key = lambda x : (x[0],x[1],x[2],x[3]))


def isBeforeMarch(m,d):
    if 0 < m <= 2:
        return True
    
    if m == 3 and d == 1:
        return True
    
    return False

def isBeforeEnd(m1,d1,m2,d2):
    if m1 > m2:
        return True
    elif m1 == m2:
        if d1 > d2:
            return True

    return False

flowers = []

# print(arr)
for flower in arr:
    s_m,s_d,e_m,e_d = flower
    if e_m < 3:
        continue

    if e_m == 3 and e_d == 1:
        continue
        
    if not flowers:
        if isBeforeMarch(s_m,s_d):
            flowers.append(flower)

    else:
        while True:
            if flowers[-1][2] >= 12:
                break
            last_flower = flowers.pop()
            if not flowers:
                if not isBeforeMarch(s_m,s_d):
                    flowers.append(last_flower)
                    if not isBeforeEnd(s_m,s_d,flowers[-1][2],flowers[-1][3]):
                        flowers.append(flower)
                else:
                    if isBeforeEnd(e_m,e_d,last_flower[2],last_flower[3]):
                        flowers.append(flower)
                    else:
                        flowers.append(last_flower)
                break

            else:
                if not isBeforeEnd(s_m, s_d,flowers[-1][2], flowers[-1][3]):
                    
                    if isBeforeEnd(e_m,e_d,last_flower[2], last_flower[3]):
                        flowers.append(flower)
                    else:
                        flowers.append(last_flower)

                else:
                    if isBeforeEnd(e_m,e_d,last_flower[2], last_flower[3]):
                        flowers.append(last_flower)
                        flowers.append(flower)
                    else:
                        flowers.append(last_flower)

                break

if len(flowers) == 0 or flowers[-1][2] >= 12:
    print(len(flowers))
else:
    print(0)