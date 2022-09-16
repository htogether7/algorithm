import math
def solution(n, stations, w):
    answer = 0
    prev = 0;
    
    for station in stations:
        start = station - w;
        end = station + w;
        distance = start - prev - 1;
        answer += math.ceil(distance / (2*w+1));
        prev = end;
        # print(station, answer);
    if prev != n:
        answer += math.ceil((n-prev) / (2*w+1));
    return answer