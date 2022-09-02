import heapq;
from collections import deque;
def solution(jobs):
    arr = jobs[::];
    arr.sort(key = lambda x : x[0]);
    arr = deque(arr);
    # map(arr)
    # print(arr);
    heap = [];
    result = 0;
    time = 0;
    while time < 1000000: 
        # print(time);
        if not arr and not heap:
            break;
            
        if len(arr) > 0 and arr[0][0] == time:
            # continue;
            # print(time);
            while len(arr) > 0 and arr[0][0] == time:
                tmp = arr.popleft();
                # print(tmp);
            # print(arr[0]);
                # print(tmp);
                heapq.heappush(heap,(tmp[1], tmp[0]));
                # print(time, heap);
        if len(heap) > 0:
            # print("hi")
            tmp = heapq.heappop(heap)
            spending_time = tmp[0];
            # print(spending_time);
            time += spending_time;
            result += (time - tmp[1]);
            # print(result, time);
            # for t in range(time, time+spending_time):
                
            while arr and arr[0][0] < time:
                tmp = arr.popleft();
                heapq.heappush(heap, (tmp[1], tmp[0]));
        else:
            # print(time);
            time += 1;        
        # print(heap);
        # print(result);
        
    # print(result);  
    return int(result / len(jobs))