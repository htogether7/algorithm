def solution(orders, course):
    answer = []
    candidates = [{} for _ in range(max(course) + 1)];
    # print(orders, course);
    
    arr = [];
    def dfs(order,s,l,target):
        sorted_arr = sorted(arr , key = lambda x : ord(x));
        tmp = "".join(sorted_arr);
        if l == target:
            if tmp in candidates[target]:
                candidates[target][tmp] += 1;
            else:
                candidates[target][tmp] = 1;
            # print(arr);
            # print(order,s,l,target,present);
            
            return;
        else:
            
            for i in range(s+1,len(order) - target + l + 2):
                # present += string[s];
                # print(i,present)
                # print(present);
                # tmp = present + order[s];
                # print(present);
                arr.append(order[i-1]);
                dfs(order,i,l+1,target);
                # print(arr, i);
                arr.pop();
                # print(arr, i)
                # print(present + order[s]);
                
    
    for string in orders:
        for count in course:
            if count <= len(string):
                dfs(string,0,0,count);
    # dfs("ABCFG", 0, 0, 2);
    
    # print(candidates);
    for candidate_dict in candidates:
        if candidate_dict:
            max_value = max(candidate_dict.values());
            if max_value < 2:
                continue;
            for key in candidate_dict.keys():
                if candidate_dict[key] == max_value:
                    answer.append(key);
    # print(candidates);
    # for i in range(2):
        # answer.sort(key= lambda x : ord(x[i]));
    answer.sort();
    print(answer);
    return answer