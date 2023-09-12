import heapq

# 초기 리스트 정의. 현재 힙 속성을 만족하지 않음
# 힙 속성: 부모 노드가 자식 노드보다 항상 작은 이진 트리
lst = [4, 15, 7, 3, 2, 8]
print("초기 리스트: ", lst) #출력값 : [4, 15, 7, 3, 2, 8]
# 현재 트리:
#      4
#    /   \
#   15    7
#  /  \  /
# 3    2 8 

# heapq.heapify(iterable): 리스트를 in-place로 힙 속성을 만족하도록 변환, 반환값은 None
# 시간 복잡도: O(N)
heapq.heapify(lst)
print("heapify(lst) 후 리스트: ", lst) #출력값 : [2, 3, 7, 4, 15, 8]
# 변환된 트리:
#      2
#    /   \
#   3     7
#  /  \  /
# 4   15 8 

# heapq.heappush(heap, elem): 힙에 원소를 추가
# 시간 복잡도: O(log N)
heapq.heappush(lst, 1)
print("heappush(lst, 1) 후 리스트: ", lst)  #출력값 : [1, 3, 2, 4, 15, 8, 7]

# heapq.heappop(heap): 힙에서 가장 작은 원소를 제거하고 그 원소를 반환
# 시간 복잡도: O(log N)
print("heappop(lst) 출력: ", heapq.heappop(lst))  #출력값 : 1
print("heappop(lst) 후 리스트: ", lst)  #출력값 : [2, 3, 7, 4, 15, 8]

# ... (여기에 추가 메서드 및 설명을 넣어주세요)

# heappushpop(heap, ele): 힙 heap에 요소 ele를 푸시하고, 힙에서 가장 작은 요소를 팝하고 반환
# 시간 복잡도: O(log N)
print("heappushpop(lst, 0) 실행 결과:", heapq.heappushpop(lst, 0))  #출력값 :  0
print("heappushpop(lst, 0) 후 리스트:", lst)  #출력값 :  [2, 3, 7, 4, 15, 8]

# heapreplace(heap, ele): 힙에서 가장 작은 요소를 팝하고, 요소 ele를 푸시
# 시간 복잡도: O(log N)
print("heapreplace(lst, 0) 실행 결과:", heapq.heapreplace(lst, 0))  #출력값 :  2
print("heapreplace(lst, 0) 후 리스트:", lst)  #출력값 :  [0, 3, 7, 4, 15, 8]