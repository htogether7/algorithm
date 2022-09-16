from collections import deque;
def solution(A, B):
    answer = 0
    
    queue_a = deque(sorted(A, reverse=True));
    queue_b = deque(sorted(B, reverse=True));
    
    while queue_a and queue_b:
        if queue_b[0] > queue_a[0]:
            answer += 1;
            queue_a.popleft();
            queue_b.popleft();
        else:
            queue_a.popleft();
    return answer