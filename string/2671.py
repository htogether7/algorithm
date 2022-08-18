import sys;
input = sys.stdin.readline;

n= input().rstrip();


# start = 0;

noise = False;

zeros = [];
tmp = [];
for i in range(len(n)):
    if i == len(n)-1:
        # print(tmp, i);
        if n[i] == "0":
            tmp.append(i);
            zeros.append(tmp);
        break;
    if n[i] == "0":
        tmp.append(i);
        if n[i+1] == "1":
            zeros.append(tmp);
            tmp = [];
                
for i in range(len(zeros)):
    if len(zeros[i]) == 1:
        if i == len(zeros)-1:
            if len(n) != zeros[i][0] +2:
                print("NOISE");
                noise = True;
                break;
        else:
            if i == 0:
                if zeros[i][0] != 0:
                    print("NOISE");
                    noise = True;
                    break;

            if len(zeros[i+1]) == 1:
                if zeros[i][0] + 2 != zeros[i+1][0]:
                    print("NOISE");
                    noise = True;
                    break;
            elif len(zeros[i+1]) > 1:
                if zeros[i][0] + 3 != zeros[i+1][0]:
                    print("NOISE");
                    noise = True;
                    break;

    else:
        if i == len(zeros)-1:
            if len(n) <= zeros[i][-1]+1:
                print("NOISE");
                noise = True;
                break;
        else:
            if i == 0:
                if zeros[i][0] != 1:
                    print("NOISE");
                    noise = True;
                    break;
            if len(zeros[i+1]) > 1:
                if zeros[i][-1] + 3 > zeros[i+1][0]:
                    print("NOISE");
                    noise = True;
                    break;

        # elif len(zeros[i+1]) > 1:
if noise == False:
    print("SUBMARINE");
# print(zeros);

# while start < len(n):
#     if n[start] == "1":
#         if n[start+1] == "0" and n[start+2] == "0":
#             start += 1;
#             while n[start] == "0":
#                 if start == len(n)-1:
#                     noise = True;
#                     print("NOISE", start);
#                     break;
#                 start += 1;
#             if noise == False:
#                 if n[start+1] == "0":
#                     start += 1;
#                 else:
#                     # 1이 2개 이상 붙어 있을 때
#                     while n[start] == "1":
#                         start += 1;
#                     # print("SUBMARINE")
#                     pass;
#         else:
#             print("NOISE",start);
#             noise = True;
#             break;
#     elif n[start] == "0":
#         if n[start+1] == "1":
#             start += 2;
#         else:
#             print("NOISE",start);
#             noise = True;
#             break;


# if noise == False:
#     print("SUBMARINE")