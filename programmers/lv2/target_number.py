from collections import deque;
def solution(numbers, target):
    answer = 0
    q = deque([]);
    nums = numbers[::];
    first = nums[0];
    q.append([first,0]);
    q.append([-first,0]);
    while q:
        num,ind = q.popleft();
        if ind != len(nums)-1:
            q.append([num+nums[ind+1], ind+1]);
            q.append([num-nums[ind+1], ind+1]);
        else:
            if num == target:
                answer += 1;
        
    return answer