from collections import deque;
def solution(progresses, speeds):
    answer = []
    q = deque(progresses)
    s = deque(speeds);
    while q:
        while q[0] < 100:
            for ind in range(len(q)):
                if q[ind] < 100:
                    q[ind] += s[ind];
        # break;
    # print(q);
        count = 0;
        while q and q[0] >= 100:
            q.popleft();
            s.popleft();
            count+= 1;
        answer.append(count);
    return answer