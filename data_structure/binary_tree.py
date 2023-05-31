class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
#     def __str__(self):
#         return str(self.data)
    

# class Tree:
#     def __init__(self):
#         self.root = None

root = Node(10)
root.left = Node(34)
root.right = Node(89)
root.left.left = Node(45)
root.left.right = Node(50)

### 이진 트리 탐색
### 재귀를 통해서 구현 가능하다!

### Pre-order NLR
def pre_order(node):
    if not node:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


# pre_order(root)

### In-order LNR
def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.data)
    in_order(node.right)

# in_order(root)

### Post-order LRN

def post_order(node):
    if not node:
        return
    
    post_order(node.left)
    post_order(node.right)
    print(node.data)

post_order(root)