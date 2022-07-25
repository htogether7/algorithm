n = input();
# print(ord("A"));
# print(ord("Z"));
# print(ord("1"));
alphas = [];
nums = [];
for i in n:
    if ord(i) >= 65 and ord(i) <= 90:
        alphas.append(i);
    else:
        nums.append(int(i));

alphas.sort();

tmp = alphas + nums;

print(''.join(alphas)+str(sum(nums)));
# print(alphas);
# print(nums);