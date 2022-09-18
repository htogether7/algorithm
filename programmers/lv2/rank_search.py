def solution(info, query):
    answer = []
    dict = {}
    lang = ["c","j","p","-"];
    job = ["b","f","-"];
    career = ["j","s","-"];
    food = ["c","p","-"];
    for l in lang:
        for j in job:
            for c in career:
                for f in food:
                    dict[l+j+c+f] = [];
    # print(dict);
    for i in info:
        lang, job, career, food, score = i.split(" ");
        info_key = lang[0] + job[0] + career[0] + food[0];
        lang_arr = [lang[0], "-"];
        job_arr = [job[0], "-"];
        career_arr = [career[0], "-"];
        food_arr = [food[0], "-"];
        score = int(score);
        for l in lang_arr:
            for j in job_arr:
                for c in career_arr:
                    for f in food_arr:
                        # if score in dict[l+j+c+f]:
                        #     dict[l+j+c+f][int(score)] += 1;
                        # else:
                        #     dict[l+j+c+f][int(score)] = 1;
                        dict[l+j+c+f].append(int(score));
    for key in dict:
        dict[key].sort();
        
    # print(dict)

    for q in query:
        lang, job, career, food_and_score = q.split(" and ");
        food, score = food_and_score.split(" ");
        query_key = lang[0]+job[0]+career[0]+food[0];
#         # print(query_key);
        score = int(score);
        
#         tmp = [];
        count = 0;
        # obj = dict[query_key];
        tmp_arr = dict[query_key]
        start = 0;
        end = len(tmp_arr)-1;
        while start <= end:
            
            mid = (start+end) // 2;
            
            if tmp_arr[mid] < score:
                start = mid + 1;
            elif tmp_arr[mid] >= score:
                end = mid - 1;
        # print(start, tmp_arr, score);
        answer.append(len(tmp_arr) - start)
        # sorted_keys = sorted(obj.keys(), reverse=True);
        # for key in sorted_keys:
        #     if key < score:
        #         break;
        #     count += obj[key];
        # answer.append(count);
        # for key in obj:
        #     if key >= score:
        #         count += obj[key];
        # answer.append(count);
    return answer;
#             for ind, char in enumerate(query_key):
#                 if query_key[ind] == "-":
#                     pass;
#                 else:
#                     if query_key[ind] != key[ind]:
#                         break;
                
#                 if ind == 3:
#                     tmp.extend(dict[key]);
#         count = 0;
#         for t in tmp:
#             if t >= score:
#                 count+= 1;
#         answer.append(count);

#     return answer