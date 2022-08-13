import sys;
# import heapq;
input = sys.stdin.readline;
s = input().rstrip();
# result = -1;

if len(s) == 1:
    print(-1);
else:
    # print(len(s));
    # print(len(s[0]*(len(s))));
    if s == s[0] * (len(s)):
        # print(True);
        print(-1);
    else:
        len_max = 0;
        if s == s[::-1]:
            print(len(s)-1);
        else:
            check_break = False;
            for length in range(len(s),-1,-1):
                if check_break:
                    break;
                for start in range(0,len(s)-length+1):
                    tmp = s[start:start+length];
                    if tmp != tmp[::-1]:
                        print(len(tmp));
                        check_break = True;
                        break;

        # for start in range(0,len(s)-1):
        #     for end in range(start+1, len(s)):
        #         tmp = s[start:end+1];
        #         if tmp == tmp[::-1]:
        #             # palins.append(end-start+1);
        #             # heapq.heappush(palins, -1 * (end-start+1))
        #             len_max = max(len_max, end-start+1);
        #     # print(tmp);
        #     # print(tmp[::-1]);
        # if len_max == 0:
        #     print(len(s));
        # else:
        #     if len(s) == len_max:
        #         print(len_max-1);
        #     else:
        #         print(len_max+1);
        #     # print(len_max-1);