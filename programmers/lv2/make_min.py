import heapq;
def solution(A,B):
    answer = 0
    a = A[::];
    b = B[::];
    a.sort();
    b.sort(reverse=True);
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    # print(a);
    # heapq.heapify(a);
    
    # b = 

    return answer