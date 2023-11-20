#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################

from collections import deque

# 데크 객체 생성
deq = deque()

# append(item): 데크의 오른쪽 끝에 item을 추가합니다.
# 반환값: 없음
# 시간 복잡도: O(1)
deq.append(1)  # 현재 데크: deque([1])
print(deq)  # 출력: deque([1])

# appendleft(item): 데크의 왼쪽 끝에 item을 추가합니다.
# 반환값: 없음
# 시간 복잡도: O(1)
deq.appendleft(0)  # 현재 데크: deque([0, 1])
print(deq)  # 출력: deque([0, 1])

# popleft(): 데크의 왼쪽 끝 요소를 제거하고 그 요소를 반환합니다.
# 반환값: 제거된 요소
# 시간 복잡도: O(1)
deq.popleft()  # 현재 데크: deque([1])
print(deq)  # 출력: deque([1])

# deq[K]: 데크의 K번째 요소를 반환합니다.
# 반환값: K번째 요소
# 시간 복잡도: O(1)
print(deq[0])  # 출력: 1
