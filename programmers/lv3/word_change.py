from collections import deque;
def solution(begin, target, words):
    if target not in words:
        return 0;
    
    check = [0 for _ in range(len(words))];
    
    q = deque([]);
    q.append((begin,0));
    while q:
        next, count = q.popleft();
        for w in words:
            diff_count = 0;
            for ind,char in enumerate(w):
                if diff_count > 1:
                    break;
                
                if w[ind] != next[ind]:
                    diff_count += 1;
            if diff_count == 1:
                if w == target:
                    return count + 1;
                else:
                    q.append((w, count + 1));
                
        # print(next,count);
        