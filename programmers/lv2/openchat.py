def solution(record):
    dict = {};
    messages = []
    for (i,rec) in enumerate(record):
        tmp = rec.split(" ");
        
        
        if tmp[0] == "Enter":
            messages.append(tmp[:2]);
            if tmp[1] not in dict:
                dict[tmp[1]] = {"nickname":tmp[2], "inds":[i]};
            else:
                dict[tmp[1]]["nickname"] = tmp[2];
                dict[tmp[1]]["inds"].append(i);
                
        elif tmp[0] == "Leave":
            messages.append(tmp[:2]);
            dict[tmp[1]]["inds"].append(i);
            
        elif tmp[0] == "Change":
            dict[tmp[1]]["nickname"] = tmp[2];
        
    results = []
    for i in messages:
        tmp = dict[i[1]]['nickname']
        if i[0] == "Enter": 
            results.append(f"{tmp}님이 들어왔습니다.");
        elif i[0] == "Leave":
            results.append(f"{tmp}님이 나갔습니다.");
    return results;
            
            