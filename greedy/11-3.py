n = input();
zero_count = 0;
one_count = 0;
for i in range(len(n)-1):
    if n[i] == "0":
        if i == len(n)-2:
            if n[i+1] == "1":
                zero_count += 1;
                one_count += 1;
                break;
            else:
                zero_count += 1;
                break;
        if n[i+1] == "1":
            zero_count += 1;
    else:
        if i == len(n)-2:
            if n[i+1] == "0":
                zero_count += 1;
                one_count += 1;
                break;
            else:
                one_count += 1;
                break;
        if n[i+1] == "0":
            one_count += 1;

print(min(zero_count, one_count));