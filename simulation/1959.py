import sys
input = sys.stdin.readline

m,n = map(int, input().split())

if m > n:
    # 가로가 짧은 사각형
    if n % 2 == 1:
        # 가로길이 홀수
        x = n // 2 + 1
        y = m - (n//2)
        count = 2 * n -1
        print(count)
        print(y,x)
    elif n % 2 == 0:
        # 가로길이 짝수
        x = n // 2 
        y = n // 2 + 1
        count = 2 * n -1
        print(count)
        print(y,x)
        

else:
    # 가로가 길거나 같은 사각형
    if m % 2 == 1:
        # 세로길이 홀수
        y = m // 2 + 1
        x = n - (m // 2)
        count = 2 * m - 2
        print(count)
        print(y,x)
    elif m % 2 == 0:
        # 세로길이 짝수
        y = m // 2 + 1
        x = m // 2
        count = 2 * m - 2
        print(count)
        print(y,x)
