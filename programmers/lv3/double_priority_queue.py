import heapq;
def solution(operations):
    # answer = []
    dict = {};
    min_heap = [];
    max_heap = [];
    
    for op in operations:
        [action, integer] = op.split(" ");
        integer = int(integer)
        if action == "I":
            heapq.heappush(min_heap, integer);
            heapq.heappush(max_heap, (-integer, integer));
            if integer in dict:
                dict[integer] += 1;
            else:
                dict[integer] = 1;
        elif action == "D":
            if integer == 1:
                if dict:
                    next = heapq.heappop(max_heap)[1];
                    # print(next, op);
                    # print(next in dict);
                    # print(next, dict);
                    count = 0;
                    while next not in dict:
                        next = heapq.heappop(max_heap)[1];
                        # count += 1;
                        # print(count);
                    if dict[next] == 1:
                        del dict[next];
                    else:
                        dict[next] -= 1;
            elif integer == -1:
                if dict:
                    next = heapq.heappop(min_heap);
                    while next not in dict:
                        next = heapq.heappop(min_heap);
                    if dict[next] == 1:
                        del dict[next];
                    else:
                        dict[next] -= 1;
    # print(dict);
    if not dict:
        return [0,0];
    else:
        max_next = heapq.heappop(max_heap)[1]
        while max_next not in dict:
            max_next = heapq.heappop(max_heap)[1]
        min_next = heapq.heappop(min_heap);
        while min_next not in dict:
            min_next = heapq.heappop(min_heap);
        return [max_next, min_next];
    # print(min_heap);
    # print(max_heap);
    # return answer