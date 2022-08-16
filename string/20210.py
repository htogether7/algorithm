import sys;
from functools import cmp_to_key;
input = sys.stdin.readline;

n = int(input());

alpha_orders = {
    "A":1,
    "a":2,
    "B":3,
    "b":4,
    "C":5,
    "c":6,
    "D":7,
    "d":8,
    "E":9,
    "e":10,
    "F":11,
    "f":12,
    "G":13,
    "g":14,
    "H":15,
    "h":16,
    "I":17,
    "i":18,
    "J":19,
    "j":20,
    "K":21,
    "k":22,
    "L":23,
    "l":24,
    "M":25,
    "m":26,
    "N":27,
    "n":28,
    "O":29,
    "o":30,
    "P":31,
    "p":32,
    "Q":33,
    "q":34,
    "R":35,
    "r":36,
    "S":37,
    "s":38,
    "T":39,
    "t":40,
    "U":41,
    "u":42,
    "V":43,
    "v":44,
    "W":45,
    "w":46,
    "X":47,
    "x":48,
    "Y":49,
    "y":50,
    "Z":51,
    "z":52,
}
count = 0;
def compare(a,b):
    # if a.isdigit() and b.isdigit():
    # for i in range(min(len(a),len(b))):
    # for i in range(1,2):
    if a[count].isdigit() and b[count].isdigit():
        if int(a[count]) < int(b[count]):
            return -1;
        elif int(a[count]) > int(b[count]):
            return 1;
        else:
            if len(a[count]) > len(b[count]):
                return 1;
            elif len(a[count]) < len(b[count]):
                return -1;
    else:
        if a[count].isdigit() and b[count].isalpha():
            return -1
        elif a[count].isalpha() and b[count].isdigit():
            return 1
        else:
            return (alpha_orders[a[count]] - alpha_orders[b[count]]);



# arr = [input().rstrip() for _ in range(n)];
arr = [];
for _ in range(n):
    tmp = input().rstrip();
    sub_arr = [];
    sub_string = "";
    for j in tmp:
        # print(j);
        if j.isdigit() == False:
            if len(sub_string) != 0:
                sub_arr.append(sub_string);
            sub_string = "";
            sub_arr.append(j);
        else:
            sub_string += j;
    # print(sub_arr);
    arr.append(sub_arr);
print(arr);
while True:
    if count == 2:
        break;
    arr.sort(key = cmp_to_key(compare));
    count += 1;

result = [];
for i in arr:
    result.append("".join(i));
print(result);
# print(arr);

# for 
# ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];


# print(arr);
