# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None


# n1 = Node("시환")

# # 연결
# n2 = Node("소현")
# n1.next = n2

# # print(n1.next.data)

# # 노드 삽입

# n3 = Node("정현")
# n1.next = n3
# n3.next = n2

# print(n1.data)
# print(n1.next.data)
# print(n1.next.next.data)

# # 노드 삭제

# n1.next = n2
# del (n3)

# print(n1.data)
# print(n1.next.data)

# #------------------------------- 위까지는 링크드 리스트 간단 구현

# ### 링크드 리스트 일반 구현

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    #헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        n = self.head
        while n.next != None:
            n = n.next
        
        n.next = Node(data)

    #모든 노드 값 출력
    def print_all(self):
        result = []
        n = self.head
        result.append(n.data)
        while n.next != None:
            n = n.next
            result.append(n.data)
        # result.append(n)
        print(result)

    #인덱스 통해 노드 알아내기
    def get_node(self, index):
        cnt = 0
        n = self.head
        while n != None:
            if cnt == index:
                return n.data
            cnt += 1
            n = n.next
        return None

    #노드 삽입
    def add_node(self, index, value):
        tmp = Node(value)
        n = self.head
        

        if index == 0:
            tmp.next = self.head
            self.head = tmp
        else:
            cnt = 0
            while n != None:
                if cnt == index-1:
                    tmp.next = n.next
                    n.next = tmp
                    break
                cnt += 1
                n = n.next


    #노드 삭제
    def delete_node(self, index):
        cnt = 0
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            del deleted_node
        else:
            d = self.get_node(index-1)
            d.next = d.next.next


        


l = LinkedList(3)
l.append(4)
l.add_node(1,2)
l.print_all()

print(l.get_node(1))