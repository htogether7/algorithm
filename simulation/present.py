from itertools import combinations
def solution(friends, gifts):
    answer = 0
    dic = {}
    n = len(friends)
    for i, user in enumerate(friends):
        dic[user] = i
        
    arr = [[0] * n for _ in range(n)]
    
    for present_string in gifts:
        a,b = present_string.split(" ")
        arr[dic[a]][dic[b]] += 1
        
    present_point = []
    
    for i in range(n):
        tmp_point = sum(arr[i])
        for j in range(n):
            tmp_point -= arr[j][i]
        present_point.append(tmp_point)

    present_count_array = [0] * n
    comb = (combinations([i for i in range(n)],2))
    for a,b in list(comb):
        if a == b:
            continue

        a_to_b = arr[a][b]
        b_to_a = arr[b][a]
        if (a_to_b != 0 or b_to_a != 0) and a_to_b != b_to_a:
            if a_to_b > b_to_a:
                present_count_array[a] += 1
            else:
                present_count_array[b] += 1
        else:
            if present_point[a] > present_point[b]:
                present_count_array[a] += 1
            elif present_point[a] < present_point[b]:
                present_count_array[b] += 1
    return max(present_count_array)