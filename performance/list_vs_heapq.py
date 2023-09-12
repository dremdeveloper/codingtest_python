import heapq
import time
import random

num_elements = 10000
lst = []
heap = []

# 일반 리스트 사용
start_time = time.time()
for _ in range(num_elements):
    val = random.randint(1, num_elements)
    lst.append(val)
    lst.sort()
list_time = time.time() - start_time

# heapq 사용
start_time = time.time()
for _ in range(num_elements):
    val = random.randint(1, num_elements)
    heapq.heappush(heap, val)
heap_time = time.time() - start_time

print(f"Insertion & sort in list took: {list_time:.6f} seconds")# 0.757835초(환경마다 달라질수 있음)
print(f"Insertion using heapq took: {heap_time:.6f} seconds")# 0.022424초(환경마다 달라질수 있음)
