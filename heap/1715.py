import sys;
import heapq;

n = int(input());
hq = [];

result = 0;
tmp = 0;
for i in range(n):
    num = int(sys.stdin.readline());
    heapq.heappush(hq, num);

while hq:
    if tmp == 0:
        tmp += heapq.heappop(hq);
    else:
        tmp += heapq.heappop(hq);
        heapq.heappush(hq, tmp);
        result += tmp;
        tmp = 0;
    # print(hq)
# result += tmp;
print(result);
