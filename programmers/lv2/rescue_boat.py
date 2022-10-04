# import heapq;
from collections import deque;
def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people);
    l = 0;
    r = len(people)-1;
    sum = 0;
    while l < r:
        sum += q[l];
        sum += q[r];
        if sum == limit:
            r -= 1;
            l += 1;
            answer += 1;
            sum = 0;
        elif sum > limit:
            r -= 1;
            answer += 1;
            sum = 0;
        elif sum < limit:
            while True:
                l += 1;
                sum += q[l]
                if sum > limit:
                    sum = 0;
                    answer += 1;
                    r -= 1;
                    break;
                elif sum == limit:
                    l += 1;
                    r -= 1;
                    sum = 0;
                    answer += 1;
                    break;
    # print(l,r);
    if l == r:
        answer += 1;
    return answer

# print(solution([50],100))