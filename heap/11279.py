import sys;
import heapq;
n = int(input());

hq = [];
for i in range(n):
    num = int(sys.stdin.readline());
    if num == 0:
        if len(hq) == 0:
            print(0);
        else:
            print(-heapq.heappop(hq));
    else:
        heapq.heappush(hq, -1 * num);
    # print(hq);

