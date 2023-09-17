#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. list 사용: 리스트에 요소를 추가한 후에 매번 정렬을 수행합니다. 
#    이 경우, append 연산은 O(1)의 시간 복잡도를 가지지만, sort() 메서드는 O(n log n)의 시간 복잡도를 가집니다. 
#    따라서 전체 작업의 시간 복잡도는 O(n^2 log n)이 됩니다.
# 2. heapq 사용: heapq는 이진 힙 자료구조를 사용하여 요소를 추가할 때마다 힙 속성을 유지합니다. 
#    heappush 연산은 O(log n)의 시간 복잡도를 가집니다. 
#    따라서 전체 작업의 시간 복잡도는 O(n log n)이 됩니다.
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
