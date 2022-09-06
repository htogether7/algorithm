from collections import Counter;

def solution(str1, str2):
    answer = 0
    small_str1 = str1.lower();
    small_str2 = str2.lower();
    
    arr_str1 = [];
    arr_str2 = [];
    
    for i in range(len(str1)-1):
        if 97 <= ord(small_str1[i]) <= 122 and 97 <= ord(small_str1[i+1]) <= 122:
            arr_str1.append(small_str1[i:i+2]);
    
    for i in range(len(str2)-1):
        if 97 <= ord(small_str2[i]) <= 122 and 97 <= ord(small_str2[i+1]) <= 122:
            arr_str2.append(small_str2[i:i+2]);
        
    # print(arr_str1);
    sumCount = Counter(arr_str1 + arr_str2);
    # print(sumCount);
    
    
    # print(arr_str2);
    str1_count = Counter(arr_str1);
    str2_count = Counter(arr_str2);
    
    intersection = 0;
    sumsection = 0;
    
    for i in sumCount:
        if sumCount[i] > 1:
            if str1_count[i] == 0 or str2_count[i] == 0:
                sumsection += sumCount[i];
            else:
                tmp_intersected = min(str1_count[i], str2_count[i]);
                intersection += tmp_intersected;
                sumsection += tmp_intersected;
                sumsection += (max(str1_count[i], str2_count[i]) - tmp_intersected);
        else:
            sumsection += sumCount[i];
    
    # print(sumsection);
    # print(intersection);
    if not sumsection:
        return 65536;
    else:
        return int((intersection / sumsection) * 65536)
