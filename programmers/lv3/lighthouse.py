import heapq
def solution(n, lighthouse):
    # if n == 2:
    #     return 1
    answer = n
    countDict = {};
    count = 0
    check = [2] * (n-1)
    for i,(a,b) in enumerate(lighthouse):
        if a not in countDict:
            countDict[a] = [i]
        else:
            countDict[a].append(i)
        
        if b not in countDict:
            countDict[b] = [i]
        else:
            countDict[b].append(i)
            
    for key in countDict:
        if (len(countDict[key]) == 1):
            check[countDict[key][0]] -= 1
            answer -= 1
    for key in countDict:
        check_turn_off = True
        for index in countDict[key]:
            if check[index] != 2:
                check_turn_off = False
                break
        
        if check_turn_off:
            for index in countDict[key]:
                check[index] -= 1
            answer -= 1
    # print(countDict)
    # print(check)
    # print(answer)
    return answer