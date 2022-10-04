import sys;
input = sys.stdin.readline;
s = input().rstrip();

isTag = False;

tags = [];
words = [];

substring = [];
result = "";
for i in s:
    # print(result);
    if i == "<":
        if not isTag:
            substring.reverse();
            result += "".join(substring);
            substring = [];
        else:
            if substring:
                # words.append("".join(substring));
                result += "".join(substring);
                substring = [];
        isTag = True;
        substring.append(i);
    elif i == ">":
        isTag = False;
        substring.append(i);
        result += "".join(substring);
        # tags.append("".join(substring));
        substring = [];
    else:
        if not isTag:
            if i == " ":
                # words.append("".join(substring));
                substring.reverse();
                result += "".join(substring) + " ";
                # words.append()
                substring = [];
            else:
                substring.append(i);
        else:
            substring.append(i);

if not isTag:
    substring.reverse();
    result += "".join(substring)
print(result);

# print(result == "noojkeab enilno egduj");
# print(tags);
# print(words);