import heapq # heapq를 쓰기 위해 필요

# 빈 힙 생성
heap = []

# 값들을 우선순위 큐에 삽입 (heappush 사용)
heapq.heappush(heap, 10)
heapq.heappush(heap, 5)
heapq.heappush(heap, 20)
heapq.heappush(heap, 1)

# 현재 우선순위 큐의 상태 출력
print(heap) # 출력: [1, 5, 20, 10]

# 우선순위 큐에서 가장 작은 요소 확인 및 제거 (heappop 사용)
print(heapq.heappop(heap)) # 출력: 1
print(heap) # 출력: [5, 10, 20]
print(heapq.heappop(heap)) # 출력: 5
print(heap) # 출력: [10, 20]