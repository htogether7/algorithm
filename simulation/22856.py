import sys;
input = sys.stdin.readline;

n = int(input())

nodes = {}
check = [0] * n
# checkCount = 1
moveCount = 0

node = 1
check[0] = 1

for _ in range(n):
    a,b,c = map(int,input().split())
    nodes[a] = [b,c]

end = 1
while nodes[end][0] != -1 or nodes[end][1] != -1:
    if nodes[end][1] == -1:
        break
    end = nodes[end][1]
# prev = 1
# print(end)
stack = [1]
while True:
    nextNodes = nodes[node]
    # for left, right in nextNodes:
    left = nextNodes[0]
    right = nextNodes[1]

    if left != -1 and check[left-1] == 0:
        # checkCount += 1
        prev = node
        moveCount += 1
        node = left
        check[left-1] = 1
        stack.append(node)
        # continue

    elif right != -1 and check[right-1] == 0:
        # checkCount += 1
        prev = node
        moveCount += 1
        node = right
        check[right-1] = 1
        stack.append(node)
        # continue
    
    elif node == end:
        break

    else:

        stack.pop()
        node = stack[-1]
        moveCount += 1
    # print(node)
print(moveCount)
