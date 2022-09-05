import sys;
input = sys.stdin.readline;

k = int(input());
n = int(input());
target = input().rstrip();

board = [list(input().rstrip()) for _ in range(n)];

order = [chr(i) for i in range(65, 65 + k)];


unknown_index = 0;
for i in range(n):
    if board[i][0] != "?":
        for j in range(k-1):
            if board[i][j] == "-":
                order[j], order[j+1] = order[j+1], order[j];
        # print(order);
    else:
        unknown_index = i;
        break;


reverse_order = list(target);

for i in range(n-1, unknown_index, -1):
    if board[i][0] != "?":
        for j in range(k-1):
            if board[i][j] == "-":
                reverse_order[j], reverse_order[j+1] = reverse_order[j+1], reverse_order[j];
    else:
        break;

# print(order);
# print(reverse_order);

result = [];
for i in range(k-1):
    if order[i] == reverse_order[i+1] and order[i+1] == reverse_order[i]:
        result.append("-");
    else:
        result.append("*");

possible = True;

for i in range(k):
    # print(order.index(chr(65+i)), reverse_order.index(chr(65+i)))
    if abs(order.index(chr(65+i)) - reverse_order.index(chr(65+i))) > 1:
        possible = False;
        print("x" * (k-1));
        break;

if possible:
    print("".join(result));
