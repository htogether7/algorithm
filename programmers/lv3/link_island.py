def solution(n, costs):
    answer = 0
    
    
    
    sorted_costs = sorted(costs, key = lambda x : x[2]);
    # print(sorted_costs);
    a,b,cost = sorted_costs[0];
    
    count = 2;
    check = [0] * n;
    answer += cost;
    check[a] = 1;
    check[b] = 1;
    
    while count != n:
        for i in sorted_costs:
            a,b,cost = i;
            if check[a] == 1 and check[b] == 1:
                continue;
            elif check[a] == 0 and check[b] == 0:
                continue;
            else:
                if check[a] == 0:
                    check[a] = 1;
                elif check[b] == 0:
                    check[b] = 1;
                answer += cost;
                count+=1;
                # print(i,answer)
                break;
    return answer;