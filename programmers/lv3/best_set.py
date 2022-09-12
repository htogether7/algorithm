def solution(n, s):
    answer = []
    if n > s:
        return [-1];
    mod = s % n;
    if mod == 0:
        div = s / n;
        return [div for _ in range(n)];
            
    else:
        div = s // n;
        tmp = [div for _ in range(n)];
        for i in range(n-1, n-1-mod, -1):
            tmp[i] += 1;
        return tmp