import re;
string = input();
# r = '\+';

# print(re.split(r, n));
arr = [];
count = 0;
plus_count = 0;
for ind, n in enumerate(string):

    if n == "+" or n == "-":
        arr.append(int(string[count:ind]));
        arr.append(string[ind]);
        count = ind + 1;
        if n == "+":
            plus_count += 1;

    if ind == len(string) - 1:
        arr.append(int(string[count:]));


while len(arr) != 1:
    for i in range(len(arr)):
        if plus_count > 0:
            if arr[i] == "+":
                tmp = arr[i-1] + arr[i+1];
                arr = arr[:i-1] + [tmp] + arr[i+2:]; # 마이너스가 마지막일 때 고려해야하는가?
                plus_count -= 1;
                break;
        else:
            if arr[i] == "-":
                tmp = arr[i-1] - arr[i+1];
                arr = arr[:i-1] + [tmp] + arr[i+2:];
                break;
print(arr[0])

