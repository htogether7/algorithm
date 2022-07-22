import sys;
n = int(sys.stdin.readline().rstrip());
n_list = list(map(int,sys.stdin.readline().rstrip().split()));
m = int(sys.stdin.readline().rstrip());
m_list = list(map(int, sys.stdin.readline().rstrip().split()));

n_list.sort();
m_list.sort();

def binary_search(target):
    start = 0;
    end = len(n_list)-1;
    while start <= end:
        mid = (start+end) // 2;
        if n_list[mid] == target:
            return True;
        elif n_list[mid] > target:
            end = mid - 1;
        elif n_list[mid] < target:
            start = mid + 1;
    return False;
result = "";
for i in m_list:
    if binary_search(i):
        result += "yes ";
    else:
        result += "no ";
print(result);
