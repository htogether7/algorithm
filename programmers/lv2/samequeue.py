from collections import deque;

def solution(queue1, queue2):
    target = (sum(queue1)+sum(queue2)) // 2;
    
    q1 = deque(queue1 + queue2);
    
    count = 0;
    
    sum1 = sum(queue1);
    sum2 = sum(queue2);

    count = 0;
    split_index = len(queue1);
    
    while sum1 != sum2:
        if sum1 > sum2:
            count += 1;
            sum1 -= q1[0];
            sum2 += q1[0];
            q1.append(q1.popleft());
            split_index -= 1;
        else:
            count += 1;
            sum1 += q1[split_index];
            sum2 -= q1[split_index];
            split_index += 1;
        # print(sum1, sum2, count);
        if count == len(q1) *2:
            count = -1;
            break;
    return count;
    

