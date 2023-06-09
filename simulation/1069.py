import sys
input = sys.stdin.readline

x,y,d,t = map(int, input().split())

def cal():
    l = (x**2+y**2)**(1/2)

    div = l // d
    mod = l % d

    # 일직선상 이동
    tmp = l
    if mod >= d/2:
        tmp = min(tmp,(d-mod) + (div+1) * t)
    else:
        tmp = min(tmp,mod + div*t)
    

    # 일직선을 벗어나서 이동
    tmp_time = 0
    if l <= d:
        tmp = min(tmp, 2*t)
    else:
        while True:
            if d*tmp_time >= l:
                break
            tmp_time+=1
        
        tmp = min(tmp, tmp_time*t)
    return tmp

print(cal())