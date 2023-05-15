import heapq
arr = [0]

h1 = [3, 4, 6, 8, 5, 7]
h2 = [3, 4, 6, 8, 5, 7]



def heappush(heap, n):
    heap.append(n)
    current_index = len(heap)-1
    while current_index > 0:
        parent_index = (current_index-1) // 2
        if heap[current_index] < heap[parent_index]:
            heap[current_index], heap[parent_index] = heap[parent_index], heap[current_index]
            current_index = parent_index
        else:
            return



def heappop(heap):
    if not heap:
        return None
    
    if len(heap) == 1:
        return heap.pop()
    
    tmp = heap[0]
    heap[0] = heap.pop()
    current_index = 0

    while True:
        if current_index*2 + 1 >= len(heap):
            return tmp
        
        next_index = current_index
        if current_index*2+2 >= len(heap):
            next_index = current_index*2+1
        else:
            if heap[current_index*2+1] <= heap[current_index*2+2]:
                next_index = current_index*2+1
            else:
                next_index = current_index*2+2

        if heap[next_index] < heap[current_index]:
            heap[next_index], heap[current_index] = heap[current_index], heap[next_index]
            current_index = next_index
            continue
        
        # if heap[current_index*2+1] < heap[current_index]:
        #     heap[current_index*2+1], heap[current_index] = heap[current_index], heap[current_index*2+1]
        #     current_index = current_index * 2 + 1
        #     continue
            
        # if heap[current_index*2+2] < heap[current_index]:
        #     heap[current_index*2+2], heap[current_index] = heap[current_index], heap[current_index*2+2]
        #     current_index = current_index * 2 + 2
        #     continue

        return tmp
    


# heappush(arr,1)
# heappush(arr,23)
# heappush(arr,14)
# heappush(arr,10)
# heappush(arr,3)
# heappush(arr,2)

# print(arr)

# arr2 = [0]
# heapq.heappush(arr2,1)
# heapq.heappush(arr2,23)
# heapq.heappush(arr2,14)
# heapq.heappush(arr2,10)
# heapq.heappush(arr2,3)
# heapq.heappush(arr2,2)
# print(arr2)

# heappush(h1, 2)
# heapq.heappush(h2,2)
# print(h1)
# print(h2)


data1 = heappop(h1)
data2 = heapq.heappop(h2)

print(data1)
print(data2)
print(h1)
print(h2)
