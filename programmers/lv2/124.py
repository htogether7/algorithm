from collections import deque;
def solution(n):
    
    num = n;
    div_num = 3;
    ind = 0;
    q = deque([]);
    while num > 0:
        # print(num, q);
        if num // div_num > 3:
            if num % div_num == 0:
                q.appendleft(3);
                num -= (3 ** (ind)) * 3;
            else:
                tmp = (num % div_num) // (3 ** ind);
                q.appendleft(tmp);
                num -= (tmp) * (3 ** (ind));
            div_num *= 3;
            ind += 1;
        else:
            if num % div_num == 0:
                q.appendleft(3);
                num -= (3 ** (ind)) * 3;
                q.appendleft((num) // div_num);
            else:
                q.appendleft((num % div_num) // 3**(ind));
                q.appendleft((num) // div_num);
                # num -= (3 ** (ind)) * (num % div_num);
            break;
        
    # print(q, n)        
    result = ""
    for i in q:
        if i == 1:
            result += "1";
        elif i == 2:
            result += "2";
        elif i == 3:
            result += "4";
            
    return result
    # print(q);
            
# for i in range(1,14):
    # print(solution(i));