import heapq;
def solution(n, k, enemy):
    answer = 0
    heap = [];
    end = min(k,len(enemy))
    for ind in range(end):
        heapq.heappush(heap, enemy[ind])
    
    while n > 0:
        if end == len(enemy):
            return len(enemy)
        heapq.heappush(heap, enemy[end])
        end+=1
        next = heapq.heappop(heap)
        n -= next
        
        if n <= 0:
            break
        
    if n == 0:
        return (end)
    elif n < 0:
        return (end-1)