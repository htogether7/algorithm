def solution(stones, k):
    answer = 0
    start = 0;
    end = 200000000;
    
    def check(mid):
        pos = -1;
        check_possible = False;
        while pos < len(stones):
            check_possible = False;
            
            if pos >= len(stones) - k:
                return True;
            
            tmp_pos = 0;
            for i in range(pos+1,pos+k+1):
                if stones[i] >= mid:
                    tmp_pos = i;
                    check_possible = True;
                    # print(pos, mid)
                    # break;
            if check_possible:
                pos = tmp_pos;
            if not check_possible:
                return False;
        
        
    while True:
        if start >= end:
            if check(start):
                return start;
            else:
                return start - 1;
        
        mid = (start+end) // 2;
        if check(mid):
            start = mid + 1;
        else:
            end = mid - 1;
        