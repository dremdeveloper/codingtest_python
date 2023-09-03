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

print(f"Using list's pop(0) took: {list_pop_time:.6f} seconds")
print(f"Using deque's popleft() took: {deque_popleft_time:.6f} seconds")
