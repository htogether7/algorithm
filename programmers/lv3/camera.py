from collections import deque;
def solution(routes):
    answer = 0
    starts = [0 for _ in range(len(routes))];
    ends = [0 for _ in range(len(routes))];
    
    for i,r in enumerate(routes):
        starts[i] = [r[0],i];
        ends[i] = ([r[1],i]);
    starts.sort(key = lambda x : x[0]);
    ends.sort(key = lambda x : x[0]);
    starts = deque(starts);
    ends = deque(ends);
    # print(starts);
    # print(ends);
    check = [0 for _ in range(len(routes))];
    count = 0;
    q = deque([]);
    while ends:
        # print(check);
        # print(starts,ends, answer);
        if not starts:
            answer += 1;
            # print(starts,ends, answer);
            break;
        else:
            if starts[0][0] <= ends[0][0]:
                q.append(starts[0][1]);
                # check[starts[0][1]] = 1;
                # count += 1;
                starts.popleft();
            else:
                if check[ends[0][1]] == 0:
                    # print(answer);
                    answer += 1;
                    while q:
                        check[q.popleft()] = 1;

                    # count = 0;
                    ends.popleft();
                else:
                    ends.popleft();
            # count += 1;
            # print(starts,ends, answer);
            # if count == 7:
            #     break;
        
    return answer;