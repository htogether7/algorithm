def solution(s):
    answer = 1000

    for i in range(1, len(s)+1):
        # i는 끊는 단위
        tmp = "";
        start = 0;
        count = 1;
        while start <= len(s)-1:
            if start == len(s) - i:
                if count == 1:
                    tmp += s[start:start+i];
                else:
                    tmp += str(count) + s[start:start+i];
                break;
            if s[start:start+i] == s[start+i:start+2*i]:
                count += 1;

            else:
                if count == 1:
                    tmp += s[start:start+i];

                else:
                    tmp += str(count)+s[start:start+i];
                    count = 1;

            start = start + i;
        # print(i, tmp);
        answer = min(answer, len(tmp));
    return answer;