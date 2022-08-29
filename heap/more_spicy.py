import heapq;

def solution(scoville, K):
    answer = 0
    h = scoville[::];
    heapq.heapify(h);
    
    while True:
        if len(h) == 1:
            if heapq.heappop(h) >= K:
                return answer;
            else:
                return -1;
        first = heapq.heappop(h);
        second = heapq.heappop(h);
        if first >= K:
            return answer;
        
        tmp = first + second * 2;
        heapq.heappush(h, tmp);
        answer += 1;