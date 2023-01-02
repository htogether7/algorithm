from collections import defaultdict
def solution(k, tangerine):
    answer = 0
    dict = defaultdict(int)
    for t in tangerine:
        dict[t] += 1
        
    dict_list = list(dict.items())
    dict_list.sort(key = lambda x : -x[1])
    
    for sort, count in dict_list:
        k -= count
        answer += 1
        if k <= 0:
            break
    return answer