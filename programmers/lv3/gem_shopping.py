def solution(gems):
    answer = []
    length = len(gems);
    target = len(set(gems));
    
    has_gem = {};
    l = 0;
    r = 0;
    has_gem[gems[l]] = 1;
    while l < length or r < length:
        # print(has_gem);
        if len(has_gem) == target:
            if not answer:
                answer.append(l+1);
                answer.append(r+1);
            else:
                if answer[1]-answer[0] > r-l:
                    answer = [l+1, r+1];
            has_gem[gems[l]] -= 1;
            if has_gem[gems[l]] == 0:
                del has_gem[gems[l]];
            l+=1;
        else:
            if r == length-1:
                break;
            r+=1
            if gems[r] in has_gem:
                has_gem[gems[r]] += 1;
            else:
                has_gem[gems[r]] = 1;

    return answer