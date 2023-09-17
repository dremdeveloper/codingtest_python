#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 알고리즘의 개념:
#    우선순위 큐는 각 원소가 우선순위를 가진 데이터의 집합에서,
#    우선순위가 가장 높은 원소를 가장 먼저 삭제하는 자료구조입니다.
#    Python의 heapq 모듈은 최소 힙을 제공하여 우선순위 큐를 구현할 수 있습니다.

# 2. 예시 입력 / 출력:
#    입력: [(1, 'Task 1'), (3, 'Task 3'), (2, 'Task 2')]
#    출력: 'Task 1', 'Task 2', 'Task 3'

# 3. 알고리즘의 시간 복잡도:
#    - 삽입: O(log n)
#    - 삭제(최소 원소 추출): O(log n)

# 4. 해당 알고리즘으로 풀 수 있는 문제 예시:
#    - 작업 스케줄링
#    - 네트워크 트래픽 제어
#    - 데이터 스트림의 중간 값 찾기
import heapq

# 우선순위 큐(최소 힙) 초기화
priority_queue = []

# 원소 삽입
heapq.heappush(priority_queue, (1, 'Task 1'))
heapq.heappush(priority_queue, (3, 'Task 3'))
heapq.heappush(priority_queue, (2, 'Task 2'))

# 큐의 모든 원소 출력 (힙 트리의 형태로 저장되어 있음)
print(priority_queue)  # 출력: [(1, 'Task 1'), (3, 'Task 3'), (2, 'Task 2')]

# 최소 원소 삭제 및 반환
print(heapq.heappop(priority_queue))  # 출력: (1, 'Task 1')
print(heapq.heappop(priority_queue))  # 출력: (2, 'Task 2')
print(heapq.heappop(priority_queue))  # 출력: (3, 'Task 3')
