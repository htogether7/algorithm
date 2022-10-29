import sys;
input = sys.stdin.readline

n, m = map(int, input().split())
times = []
for _ in range(n):
    times.append(int(input()))
time = 1
while True:
    tmp = 0
    for t in times:
        tmp += (time // t)

    if tmp < m:
        time *= 2
    else:
        break
start = time // 2
end = time

answer = end

while start <= end:
    if start == end:
        # answer = start
        tmp = 0
        for t in times:
            tmp += (start // t)
        if tmp >= m:
            answer = start
        break
    else:
        mid = (start+end) // 2
        tmp = 0
        for t in times:
            tmp += (mid // t)
        
        if tmp < m:
            start = mid+1
        elif tmp >= m:
            end = mid-1
            answer = mid

        # print(start,end)

# print(start,end)
print(answer)

# print(time)
# print(times)