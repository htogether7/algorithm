import heapq;
def solution(n, works):
    answer = 0
    heap = [];
    for w in works:
        heapq.heappush(heap, (-w, w));
    
    while n > 0:
        if not heap:
            break;
        next = heapq.heappop(heap)[1];
        next -= 1;
        # print(next);
        if next > 0:
            heapq.heappush(heap, (-next, next));
        n -= 1;
        # break;
    # print(heap)
    if not heap:
        return answer;
    else:
        for h in heap:
            answer += h[1] ** 2;
        return answer;
    