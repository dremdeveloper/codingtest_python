#############################################################
# | cafe       | http://cafe.naver.com/dremdelover          |
# | Q&A        | https://open.kakao.com/o/gX0WnTCf          |
# | business   | ultrasuperrok@gmail.com                    |
#############################################################
# 1. 리스트에서 pop(0) 사용: 리스트에서 pop(0) 메서드를 사용하면 리스트의 첫 번째 요소를 제거하고, 
#    나머지 요소들을 한 칸씩 앞으로 이동합니다. 이 때문에 이 연산의 시간 복잡도는 O(n)입니다. 
#    여기서 n은 리스트의 길이입니다. 반복적으로 pop(0)을 호출하면 전체 시간 복잡도는 O(n^2)가 됩니다.
#
# 2. deque에서 popleft() 사용: deque 자료구조에서 popleft() 메서드를 사용하면, 첫 번째 요소를 상수 시간에 제거할 수 있습니다. 
#    이 메서드의 시간 복잡도는 O(1)입니다. 따라서, 반복적으로 popleft()를 호출하면 전체 시간 복잡도는 O(n)이 됩니다.

import time
from collections import deque

num_elements = 100000

# 리스트에서 pop(0) 사용
lst = list(range(num_elements))
start_time = time.time()
while lst:
    lst.pop(0)
list_pop_time = time.time() - start_time

# deque에서 popleft() 사용
dq = deque(range(num_elements))
start_time = time.time()
while dq:
    dq.popleft()
deque_popleft_time = time.time() - start_time

print(f"Using list's pop(0) took: {list_pop_time:.6f} seconds")# 1.152777초(환경마다 다를 수 있음)
print(f"Using deque's popleft() took: {deque_popleft_time:.6f} seconds")# 0.019073초(환경마다 다를 수 있음)
