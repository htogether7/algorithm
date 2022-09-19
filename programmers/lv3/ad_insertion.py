from collections import deque, Counter;
def solution(play_time, adv_time, logs):
    answer = ''
    starts = [];
    ends = [];
    
    for log in logs:
        # print(log);
        start,end = log.split("-");
        hour, minute, second = map(int,start.split(":"));
        starts.append(hour * 3600 + minute * 60 + second);
        hour, minute, second = map(int,end.split(":"));
        ends.append(hour * 3600 + minute * 60 + second);
    
    starts.sort();
    ends.sort();
    
    # starts = deque(starts);
    # ends = deque(ends);
    dict_starts = Counter(starts);
    dict_ends = Counter(ends);
    
    starts_keys = list(Counter(starts).keys());
    ends_keys = list(Counter(ends).keys());
    
    starts_ind = 0;
    ends_ind = 0;
    
    points = {};
    count = 0;
    
    while starts_ind < len(starts_keys) or ends_ind < len(ends_keys):
        if starts_ind < len(starts_keys) and starts_keys[starts_ind] <= ends_keys[ends_ind]:
            count += dict_starts[starts_keys[starts_ind]];
            points[starts_keys[starts_ind]] = count;
            starts_ind += 1;
        elif starts_ind == len(starts_keys) or starts_keys[starts_ind] > ends_keys[ends_ind]:
            count -= dict_ends[ends_keys[ends_ind]];
            points[ends_keys[ends_ind] ] = count;
            ends_ind += 1;
        
    point_keys = deque(list(points.keys()));
    # print(point_keys);
    hour,minute,second = map(int,play_time.split(":"));
    board = [0] * (hour*3600+minute*60+second+1) ;
    board_count = 0;
    for i in range(len(board)):
        if point_keys and i == point_keys[0]:
            board_count = points[i];
            point_keys.popleft();
        board[i] = board_count;
    # print(points)
    # print(board[5459]);
    
    hour,minute,second = map(int,adv_time.split(":"));
    l = 0;
    r = hour * 3600 + minute * 60 + second;
#     # print(r);
#     # print(board[0:10]);
    answer = 0;
    now_sum = sum(board[0:r]);
#     # print(now_sum);
    max_sum = now_sum
#     # count = 0;
    while r < len(board):
        # if count == 10:
#             # break;
        now_sum -= board[l];
        now_sum += board[r];
        
        l += 1;
        r += 1;
        if now_sum > max_sum:
            # print(l);
            max_sum = now_sum;
            answer = l;
    # print(answer);
# #     # print(sum(board[5459: 6315]));
# #     # print(max_sum);
# #     # print(board[5459], board[5864])
    answer_hour = 0;
    answer_minute = 0;
    answer_second = 0;
    answer_hour = answer // 3600;
    answer -= answer_hour * 3600;
    answer_minute = answer // 60;
    answer -= answer_minute * 60;
    answer_second = answer;
    
    answer_hour = str(answer_hour)
    answer_minute = str(answer_minute);
    answer_second = str(answer_second);
    
    tmp = "";
    if len(answer_hour) == 1:
        answer_hour = "0" + answer_hour;
    
    if len(answer_minute) == 1:
        answer_minute = "0" + answer_minute;
    
    if len(answer_second) == 1:
        answer_second = "0" + answer_second;
    
    answer = ":".join([answer_hour,answer_minute,answer_second]);
        
    return answer