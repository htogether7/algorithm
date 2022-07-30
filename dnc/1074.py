import sys;
input = sys.stdin.readline;
n, r, c = map(int, input().split());
answer = 0;
while n >= 1:
    tmp_r = r //2**(n-1);
    tmp_c = c //2**(n-1);
    if tmp_r == 1:
        answer += ((2**(n-1))**2)*2;
    if tmp_c == 1:
        answer += (2**(n-1))**2;
    r -= tmp_r *(2**(n-1));
    c -= tmp_c * (2**(n-1));

    n -= 1;
print(answer);